from datetime import date
import os
import pandas as pd
import mysql.connector

from send_email import send_reminder_email, send_cancelation_email

TEST_EMAIL_ADDRESS = "nicola.szwaja@gmail.com"

def load_df_from_db(password):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password=password,
        database="workshops_data",
    )
    print("connected to database :)")
    return mydb

def check_payments(mydb):
    # Select all records where the payment deadline has passed and the participant has not paid
    query = """
    SELECT * FROM workshop_participants
    INNER JOIN workshops ON workshop_participants.workshop_id = workshops.workshop_id
    WHERE due_date <= CURDATE() AND has_paid = 0;
    """
    df_payments = pd.read_sql(query, mydb)
    # Iterate through the selected records
    email_counter = 0
    for _, row in df_payments.iterrows():
        send_reminder_email(
            subject="Dance workshop reminder",
            receiver=TEST_EMAIL_ADDRESS,
            name=row["name"],
            workshop_name=row["workshop_name"],
            workshop_date=row["workshop_date"],
            additional_note=f"A friendly reminder that the payment deadline for the workshop has passed on {row['due_date']}. Please remember to pay for the workshop.",
        )
        email_counter += 1

    print(f"Sent {email_counter} emails with payments reminders.")
    return

def send_reminders(mydb):
    # Select all records where the payment deadline has passed and the participant has not paid
    query = """
    SELECT * FROM workshop_participants
    INNER JOIN workshops ON workshop_participants.workshop_id = workshops.workshop_id
    WHERE workshop_date BETWEEN CURDATE() AND CURDATE() + INTERVAL 7 DAY;
    """
    df_reminders = pd.read_sql(query, mydb)
    # Iterate through the selected records
    email_counter = 0
    for _, row in df_reminders.iterrows():
        send_reminder_email(
            subject="Dance workshop reminder",
            receiver=TEST_EMAIL_ADDRESS,
            name=row["name"],
            workshop_name=row["workshop_name"],
            workshop_date=row["workshop_date"]
        )
        email_counter += 1

    print(f"Sent {email_counter} emails with payments reminders.")
    return

def cancell_low_participation_workshops (mydb):
    # Select all records where the payment deadline has passed and the participant has not paid
    query = """
    SELECT * FROM workshop_participants
    INNER JOIN workshops ON workshop_participants.workshop_id = workshops.workshop_id
    WHERE curr_participants < max_participants/2 AND workshop_date = CURDATE() + INTERVAL 1 DAY;
    """
    df_reminders = pd.read_sql(query, mydb)
    # Iterate through the selected records
    email_counter = 0
    if not df_reminders.empty:
        for _, row in df_reminders.iterrows():
            send_cancelation_email(
                subject="Dance workshop reminder",
                receiver=TEST_EMAIL_ADDRESS,
                name=row["name"],
                workshop_name=row["workshop_name"],
                workshop_date=row["workshop_date"]
            )
            email_counter += 1

    print(f"Sent {email_counter} emails with payments reminders.")
    return

if __name__ == "__main__":
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    mydb = load_df_from_db(DB_PASSWORD)
    check_payments(mydb)
    send_reminders(mydb)
    cancell_low_participation_workshops(mydb)
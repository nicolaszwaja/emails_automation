import os
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="vectra123",
    database="workshops_data",
)

mycursor = mydb.cursor()

sqlParticipantsFormula = """
INSERT INTO workshop_participants (participant_id, name, email_address, workshop_id, sign_up_date, has_paid)
VALUES (%s, %s, %s, %s, %s, %s)
"""

participants_info = [
    (1, "John Doe", "john.doe@email.com", 1, "2023-01-05", 1),
    (2, "Jane Smith", "jane.smith@email.com", 2, "2023-01-10", 0),
    (3, "Bob Johnson", "bob.johnson@email.com", 3, "2023-01-15", 1),
    (4, "Alice Brown", "alice.brown@email.com", 4, "2023-01-20", 0),
    (5, "Charlie White", "charlie.white@email.com", 1, "2023-01-25", 1),
    (6, "Emily Black", "emily.black@email.com", 2, "2023-01-08", 0),
    (7, "David Green", "david.green@email.com", 3, "2023-01-12", 1),
    (8, "Grace Red", "grace.red@email.com", 4, "2023-01-18", 0),
    (9, "Frank Yellow", "frank.yellow@email.com", 1, "2023-01-22", 1),
    (10, "Helen Purple", "helen.purple@email.com", 2, "2023-01-27", 0),
    (11, "Isaac Orange", "isaac.orange@email.com", 3, "2023-01-30", 1),
    (12, "Julia Pink", "julia.pink@email.com", 4, "2023-01-03", 0),
    (13, "Kevin Brown", "kevin.brown@email.com", 1, "2023-01-14", 1),
    (14, "Linda Gray", "linda.gray@email.com", 2, "2023-01-16", 0),
    (15, "Mike Silver", "mike.silver@email.com", 3, "2023-01-28", 1),
]

mycursor.executemany(sqlParticipantsFormula, participants_info)
mydb.commit()


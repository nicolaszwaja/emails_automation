from datetime import date
import pandas as pd
from send_email import send_email

SHEET_ID = "1x1bu9t8g1M9zjzLuLvNHFL7f8AUfaTgRy-7eyrKRH8M"
SHEET_NAME = "registrations"
SHEET_NAME_INFO = "workshop_info"
URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"

def load_df(url):
    parse_dates = ["sign_up_date",	"due_date"]
    df = pd.read_csv(url, parse_dates=parse_dates)
    return df


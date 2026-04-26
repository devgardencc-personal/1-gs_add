import gspread
from datetime import datetime
import os
from dotenv import load_dotenv


def add_record_to_sheet(sheet_id, name):
    gc = gspread.service_account(filename="credentials.json")
    sh = gc.open_by_key(sheet_id)
    worksheet = sh.sheet1
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M")

    row_to_insert = [current_date, name]

    worksheet.append_row(row_to_insert)
    print(f"Успешно добавлена новая запись: {row_to_insert}")


if __name__ == "__main__":
    load_dotenv()
    GS_ID = os.getenv("GS_ID")
    PERSON_NAME = "IVAN IVANOV"

    add_record_to_sheet(GS_ID, PERSON_NAME)

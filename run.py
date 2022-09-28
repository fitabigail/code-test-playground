import gspread
from google.oauth2.service_account import Credentials
import re

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('event_booking')

rooms = SHEET.worksheet('rooms')
data = rooms.get_all_values()
print(data)


def is_valid_mobile_num(mobile_num):

    pattern = re.compile("(0|35?[-\s]?[6-9][0-9]){9}")
    return pattern.match(mobile_num)

mobile_num = input("Enter your mobile number:")  

if is_valid_mobile_num(mobile_num):
    print(f"{mobile_num } is a valid mobile number.")
else:
    print(f"{mobile_num } is not a valid mobile number.") 






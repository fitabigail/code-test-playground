import gspread
from google.oauth2.service_account import Credentials
import re

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("event_booking")

"""
* The mobile number must be '9' digits long.
* The mobile can have '10' if including '0' at the starting.
* The mobile can have '13' digits if including Ireland prefix '+353' at the starting.
* First should contain number between [1 - 9].
* The rest '8' digit can contain any number between [0 - 9].
0879199932
"""

phone_num = input("Enter your mobile number(exemple: 879199932|0879199932|+353-879199932):")

pattern = re.compile("(0|[\+]?353)?[-\s]?[1-9][0-9]{8}")

if pattern.match(phone_num):
    print(f"{phone_num} is a valid number.")

else:
    print(f"{phone_num} is not a valid number. Please ")    





rooms = SHEET.worksheet("rooms")
data = rooms.get_all_values()
print(data)



"""

def is_valid_mobile_num(mobile_num):

    pattern = re.compile("(0|[\+]?353)?[-\s]?[1-9][0-9]{8}")
    return pattern.match(mobile_num)


mobile_num = input("Enter your mobile number:")

if is_valid_mobile_num(mobile_num):
    print(f"{mobile_num } is a valid mobile number.")
else:
    print(f"{mobile_num } is not a valid mobile number.")
"""
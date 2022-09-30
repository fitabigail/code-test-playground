import gspread
from google.oauth2.service_account import Credentials
import datetime
from datetime import datetime
import re
import pyfiglet
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("event_booking")


MSG = 'Welcome To RoseSaloon'
FRONT = 'standard'


def print_welcome_msg():
    f = pyfiglet.Figlet(font=FRONT)    
    print(Fore.YELLOW + Style.BRIGHT + f.renderText(MSG))
    print(rose_display)


"""
    prints the image of the rose from https://text-symbols.com/ascii-art/#all_cats
"""


rose_display = \
"""
──────────────▒███░───░████████▒ 
───────────█████▒░█████░▒▒▒▒▒▒█████ 
──────────██▒▒▒▒██████████████▒▒▒██░ 
─────────██▒▒▒▒███▒██▒██▒▒█████▒░▒██ 
─────────█░▒▒▒██▒████████████▒█▒▒▒█░ 
─────────█▒▒▒▒██▒▒▒░▓▓▒░▓▒▒████▒▒██ 
─────────█▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒█▒█░▒████ 
─────███████████▒▒▒▒▒▒▒▒██████▒██▓▒███ 
─────██▒▒▒▒▒▒█████▒▒▒▒▒▒▒▒█████▒▒▒▒▒██ 
───────██▒▒▒▒▒▒▒▓██████▒▒▒▒▒██▒▒▒▒▒▒███ 
────█████▒▒▒▒▒▒▒▒▒▒████▒▒▒██▒▒▒▒▒▒███ 
────██▒▒▒███▒▒▒▒▒▒▒▒▒▒▓█████▒▒▒▒▒███ 
────███▒▒▒▒███▒▒▒▒▒▒▒▒▒▒▒███▓▒▒███ 
──────█████▒▒████▒▒▒▒▒▒▒▒▒▒█████ 
─────────████▒▒██████▒▒▒▒█████ 
────────────███▒▒██████████ 
──────────────████▓──█▓█ 
────────────────────████ 
────────────────────█░█─────█████████ 
────────────────────█▓█───█████████████ 
──░█████████───────████──██▓███▒▓████ 
─█████████████─────█░███████░██████ 
───████░▒███▒██────█▓██████████ 
─────█████▓▒█████─████ 
─────────██████████▓█ 
──────────────────█▓█────████▒█▓▒█ 
─────────────────█▓██──█████████████ 
─────────────────█▓█──██▒████░█████ 
────────────────██████████▒██████ 
────────────────█▓███████████ 
───────────────████ 
───────────────█▒█ 
───────────────███ 
"""


print_welcome_msg()

my_string = str(input('Enter date(mm/dd/yyyy):'))
my_date = datetime.strptime(my_string, "%m/%d/%Y") 
print(my_date)


    
"""
* The mobile number must be '9' digits long.
* The mobile can have '10' if including '0' at the starting.
* The mobile can have '13' digits if including 
Ireland prefix '+353' at the starting.
* First should contain number between [1 - 9].
* The rest '8' digit can contain any number between [0 - 9].
0879199932
"""

phone_num = input("Enter your mobile number:")

pattern = re.compile("(0|[\+]?353)?[-\s]?[1-9][0-9]{8}")

if pattern.match(phone_num):
    print(f"{phone_num} is a valid number.")

else:
    print(f"{phone_num} is an invalid number.(Example: 0879199932|+353-879199932)")
# 3rd party imports
import gspread
from google.oauth2.service_account import Credentials

# Set scope and global variables
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('blackjack_users')
USERS = SHEET.worksheet('users')


def get_login_data():
    """
    Extract login data from googlesheet to validate user
    data provided
    """
    users_login = USERS.get_all_records()
    return users_login


def update_login_data(data):
    """
    Update user googlesheet with new username and
    password data input by the user
    """
    USERS.append_row(data)
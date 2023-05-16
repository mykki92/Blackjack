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


def validate_user_login(user, password):
    """
    Function to check if the provided username already exists, and
    that the username and password entered are valid. If the input
    provided is invalid an error will be printed to the user
    """
    try:
        if len(user) < 6 or len(password) < 6:
            raise ValueError(
                "Username and Password should be at least 6 characters"
            )
    except ValueError as v:
        print(f"\nInvalid Input: {v}")
        return False
    try:
        existing_user = get_login_data()
        for ind in existing_user:
            if ind["USERNAME"] == user:
                raise ValueError(
                    "\nUsername already exist"
                )
    except ValueError as e:
        print(f"\nInvalid Username: {e}")
        return False
    try:
        if not (isinstance(user, str) or isinstance(password, str)):
            raise TypeError(
                "\nEnter details using letters only"
            )
    except TypeError as m:
        print(f"Invalid user input: {m}")
        return False
    else:
        print("\nSign Up confirmed....")
        return True

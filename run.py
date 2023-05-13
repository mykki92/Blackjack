# Python imports
import random
import sys
import time
import os

# Internal imports
from gsheet import get_login_data
from gsheet import update_login_data
from gsheet import validate_user_login

current_user = {'name': 'Remo'}


def homeTitle():
    """
    Function to display head of the game
    """
    print("==============================================================================")
    time.sleep(1)
    print("$$$$$$$\  $$\                     $$\                               $$\ ")         
    print("$$  __$$\ $$ |                    $$ |                              $$ | ")        
    print("$$ |  $$ |$$ | $$$$$$\   $$$$$$$\ $$ |  $$\ $$\  $$$$$$\   $$$$$$$\ $$ |  $$\ ")   
    print("$$$$$$$\ |$$ | \____$$\ $$  _____|$$ | $$  |\__| \____$$\ $$  _____|$$ | $$  | ")  
    print("$$  __$$\ $$ | $$$$$$$ |$$ /      $$$$$$  / $$\  $$$$$$$ |$$ /      $$$$$$  / ")   
    print("$$ |  $$ |$$ |$$  __$$ |$$ |      $$  _$$<  $$ |$$  __$$ |$$ |      $$  _$$< ")   
    print("$$$$$$$  |$$ |\$$$$$$$ |\$$$$$$$\ $$ | \$$\ $$ |\$$$$$$$ |\$$$$$$$\ $$ | \$$\ ")  
    print("\_______/ \__| \_______| \_______|\__|  \__|$$ | \_______| \_______|\__|  \__| ") 
    print("======================================$$\   $$ |============================== ")                                
    print("                                      \$$$$$$  | ")                               
    print("                                       \______/ ")                                 
    time.sleep(1)
    print("         /\                 .-~~-.          .-~~~~-__-~~~~-.          /\ ")
    print("       .'  `.              {      }        {                }       .'  `. ")
    print("      '      `.         .-~-.    .-~-.      \              /      .'      `. ")
    print("   .'          `.      {              }      `.          .'      <          > ")
    print("  {              }      `.__.'||`.__.'         `.      .'         `.      .' ")
    print("   ~-...-||-...-~             ||                 `.  .'             `.  .' ")
    print("        '--`                 '--`                  \/                 \/ ")
    time.sleep(1)
    print("==============================================================================")


def check_existing_user():
    """
    Checks if user already has a login, if yes asks them to log in,
    if no asks them to sign up
    """
    exist_check = input("Have you played before? Y/N\n")
    if exist_check.upper() == "Y":
        sign_in()
    elif exist_check.upper() == "N":
        add_new_user()
    else:
        print("Invalid input, type Y or N")
        time.sleep(1)
        check_existing_user()


def add_new_user():
    """
    Validates new login data provided by the user and updates the
    googlesheet with new details
    """
    time.sleep(1)
    print("\nSIGN UP HERE!!")
    time.sleep(1)
    print("\nUsername and Password are case sensitive")
    print("Username and Password should be at least 6 characters")
    time.sleep(1)
    user_input = input("\nEnter New Username:\n")
    time.sleep(1)
    user_password = input("\nEnter New Password: \n")
    time.sleep(1)

    validate = validate_user_login(user_input, user_password)
    if validate:
        login = [user_input, user_password]
        update_login_data(login)
        time.sleep(2)
        os.system('clear')
        sign_in()
    else:
        time.sleep(2)
        add_new_user()


def sign_in():
    """
    Validates the users login information by comparing against
    data stored in the googlesheet
    """
    time.sleep(1)
    print("\nLOGIN TO PLAY BLACKJACK!")
    time.sleep(1)
    username = input("\nUsername: \n")
    time.sleep(1)
    password = input("\nPassword: \n")

    logins = get_login_data()
    check_login = 0
    for data in logins:
        if username == data['USERNAME']:
            if password == data['PASSWORD']:
                print("\nLog in successful!")
                time.sleep(2)
                os.system('clear')
                current_user['name'] = data['USERNAME']
                print(f"\nWelcome back {current_user['name']}!")
            else:
                print("Incorrect password, try again")
                sign_in()
        else:
            check_login += 1
    if check_login == len(logins):
        print("User does not exist, try again")
        check_existing_user()

homeTitle()
check_existing_user()

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
    Function to display the game title with card suit logos
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


def gameTitle():
    """
    Function to display the game title above the start of the game without the suit logos
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
    print("==============================================================================")

def check_existing_user():
    """
    Checks if user already has a login, if yes asks them to log in,
    if no asks them to sign up
    """
    exist_check = input("Have you played here before? Y/N\n")
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
    user_password = input("\nEnter New Password: \n")
    time.sleep(1)

    validate = validate_user_login(user_input, user_password)
    if validate:
        login = [user_input, user_password]
        update_login_data(login)
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
                time.sleep(1)
                os.system('clear')
                current_user['name'] = data['USERNAME']
                gameTitle()
                print(f"\nWelcome back {current_user['name']}!")
            else:
                print("Incorrect password, try again")
                sign_in()
        else:
            check_login += 1
    if check_login == len(logins):
        print("User does not exist, try again")
        check_existing_user()

def gameRules():
    """
    Asks the player if they would like to see the game rules before they start the game
    """
    rules = input("Would you like to see the game rules? Y/N\n")
    if rules.upper() == "Y":
        displayGameRules()
    elif rules.upper() == "N":
        input("Ready to play? Y/N\n")
        gameRules()
    else:
        print("Invalid input, type Y or N")
        gameRules()


def displayGameRules():
    """
    Function that prints the game rules to the console once the player has signed in
    """
    print("Starting with 2 cards, try to get as close to 21 as possible.")
    time.sleep(1)
    print("Going over 21 is a bust and you will lose your bet.")
    time.sleep(1)
    print("Numbered cards are worth the value on the card.")
    time.sleep(1)
    print("Kings, Queens and Jacks are worth 10.")
    time.sleep(1)
    print("Aces are worth 1 or 11, depending on the value of your other card.")
    time.sleep(1)
    print("Press 'H' to hit and take another card.")
    time.sleep(1)
    print("Press 'S' to stand and stop taking cards.")
    time.sleep(1)
    print("On your first turn you can press 'D' to double down and increase your bet.")
    time.sleep(1)
    print("In the event of a tie the bet will be returned to the player.")




homeTitle()
check_existing_user()
gameRules()


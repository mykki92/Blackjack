# Python imports
import random
import sys
import time
import os

# Internal imports
from gsheet import getLoginData
from gsheet import updateLoginData
from gsheet import validateUserLogin
from gsheet import updateChipsBalance

# Global variables using Unicode code points
# to set symbols for card suits
SPADES = chr(9824)
CLUBS = chr(9827)
HEARTS = chr(9829)
DIAMONDS = chr(9830)
CARDBACK = 'cardback'

current_user = {'name': 'password'}


def homeTitle():
    """
    Function to display the game title with card suit logos. Lettering was
    created using ASCII art generator (https://patorjk.com/)
    """
    print("=================================================================")
    time.sleep(1)
    print("$$$$$$$  $$                  $$                          $$ ")
    print("$$    $$ $$                  $$                          $$ ")
    print("$$    $$ $$  $$$$$$   $$$$$$ $$   $$ $$   $$$$$$  $$$$$$ $$    $$ ")
    print("$$$$$$$  $$       $$ $$      $$  $$           $$ $$      $$   $$ ")
    print("$$    $$ $$  $$$$$$$ $$      $$$$$   $$  $$$$$$$ $$      $$$$$$ ")
    print("$$    $$ $$ $$    $$ $$      $$  $$  $$ $$    $$ $$      $$   $$ ")
    print("$$$$$$$  $$  $$$$$$$  $$$$$$ $$   $$ $$  $$$$$$$  $$$$$$ $$    $$ ")
    print("                                     $$ ")
    print("===============================$$    $$==========================")
    print("                                $$$$$$ ")


def checkExistingUser():
    """
    Checks if user already has a login, if yes asks them to log in,
    if no asks them to sign up
    """
    user_check = input("Welcome! Do you have an account here? Y/N\n")
    if user_check.upper() == "Y":
        os.system('clear')
        homeTitle()
        signIn()
    elif user_check.upper() == "N":
        os.system('clear')
        homeTitle()
        addNewUser()
    else:
        print("Invalid input, type Y or N")
        time.sleep(1)
        checkExistingUser()


def addNewUser():
    """
    Validates new login data provided by the user and updates the
    googlesheet with new details
    """
    time.sleep(1)
    print("\nCreate an account here and get 5000 chips to start playing!")
    time.sleep(1)
    print("\nUsername and Password are case sensitive")
    print("Username and Password should be at least 6 characters")
    user_input = input("\nEnter New Username:\n")
    user_password = input("\nEnter New Password: \n")
    time.sleep(1)

    validate = validateUserLogin(user_input, user_password)
    if validate:
        login = [user_input, user_password, 5000]
        updateLoginData(login)
        time.sleep(2)
        os.system('clear')
        homeTitle()
        signIn()
    else:
        time.sleep(2)
        addNewUser()


def signIn():
    """
    Validates the users login information by comparing against
    data stored in the googlesheet
    """
    time.sleep(1)
    print("\nSIGN IN TO PLAY BLACKJACK!")
    username = input("\nUsername: \n")
    password = input("\nPassword: \n")

    logins = getLoginData()
    check_login = 0
    for data in logins:
        if username == data['USERNAME']:
            if password == data['PASSWORD']:
                print("\nSign in successful!")
                time.sleep(2)
                os.system('clear')
                current_user['name'] = data['USERNAME']
                current_user['chips'] = data['CHIPS']
                homeTitle()
                print(f"\nWelcome back {current_user['name']}!")
                print(f"You have {current_user['chips']} chips!")
            else:
                print("Incorrect password, try again")
                signIn()
        else:
            check_login += 1
    if check_login == len(logins):
        print("User does not exist, try again")
        checkExistingUser()


def gameMenu():
    """
    Asks the player if they would like to see the game rules before
    they start the game
    """
    print("What would you like to do?\n")
    print("Press I for game instructions")
    print("Press S to start the game")
    print("Press X to exit")
    menu_selection = input("Type your choice here: \n")
    if menu_selection == "i":
        displayGameRules()
    elif menu_selection == "s":
        startGame()
    elif menu_selection == "x":
        exitGame()
    else:
        print("Invalid input, type i, s or x ")
        gameMenu()


def displayGameRules():
    """
    Function that prints the game rules to the console once the player has
    signed in
    """
    os.system('clear')
    homeTitle()
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
    print("On your first turn you can press 'D' to double down.")
    time.sleep(1)
    print("You can increase your bet up to the value of your initial bet.")
    time.sleep(1)
    print("In the event of a tie the bet will be returned to the player.")
    startGame()


def startGame():
    """
    Function to let the player start the game, go back to the rules or
    exit the game
    """
    start_game = input("Ready to play Blackjack? Y/N/EXIT\n")
    if start_game.upper() == "Y":
        os.system('clear')
        homeTitle()
        playBlackjack()
    elif start_game.upper() == "N":
        os.system('clear')
        homeTitle()
        gameMenu()
    elif start_game.upper() == "EXIT":
        exitGame()
    else:
        print("Invalid input, type Y, N or EXIT")
        startGame()


def exitGame():
    """
    Function to display a screen before the player exits the game
    giving them the option to go back and look at the rules or
    restart the game
    """
    os.system('clear')
    homeTitle()
    leave_game = input("Deposit your chips and leave the game? Y/N\n")
    if leave_game.upper() == "Y":
        print('Thanks for playing, come again soon!')
        time.sleep(2)
        sys.exit()
    elif leave_game.upper() == "N":
        time.sleep(1)
        os.system('clear')
        homeTitle()
        gameMenu()
    else:
        print("Invalid input, type Y or N")
        exitGame()


def playBlackjack():
    chips = current_user['chips']

    # Main game loop that keeps count of the players money, places their
    # bets, deals the cards and handles player moves. Once all moves are
    # made the final hands are shown, the result is evaluated and the
    # winnings are added to or taken from the players account
    while True:
        # Checks if the player has money to bet, restarts the game with
        # 5000 chips if the player has bust
        if chips <= 0:
            print("Bust! Looks like you're outta luck!")
            more_chips = input("Press $ to get more chips! ")
            if more_chips == "$":
                getChips(chips)
                print("5000 chips added to your account!")
                time.sleep(2)
                os.system('clear')
                homeTitle()
                playBlackjack()

        # Player places their bet at the start of each round
        print('Chips:', chips)
        bet = placeBet(chips)

        # Deals two cards each to the dealer and the player
        deck = cardDeck()
        dealerHand = [deck.pop(), deck.pop()]
        playerHand = [deck.pop(), deck.pop()]

        # Handle player actions, lets the player hit, stand or double down
        # on their bet. Loops until the player stands or busts
        print('Bet:', bet)
        while True:
            showHands(playerHand, dealerHand, False)
            print()

            # Evaluates the value of the players hand, breaks the loop
            # and busts if the value is over 21
            if handValue(playerHand) > 21:
                break

            # Executes the players move, either H, S or D to hit, stand
            # or double down
            move = playerMove(playerHand, chips - bet)

            # Double down, player can increase their bet
            # Will also draw another card
            if move == 'D':
                additionalBet = placeBet(min(bet, (chips - bet)))
                bet += additionalBet
                print(f'Bet increased to {bet}.')
                print('Bet:', bet)

            # Draws another card if the player has chosen to hit or double down
            if move in ('H', 'D'):
                newCard = deck.pop()
                rank, suit = newCard
                print(f'You drew a {rank} of {suit}.')
                playerHand.append(newCard)

                # Bust if the player hand is over 21
                if handValue(playerHand) > 21:
                    continue

            # Stand or double down stops the players turn
            if move in ('S', 'D'):
                break

        # Handles the dealer actions
        if handValue(playerHand) <= 21:
            while handValue(dealerHand) < 17:
                # The dealer hits
                print('Dealer hits...')
                dealerHand.append(deck.pop())
                showHands(playerHand, dealerHand, False)

                if handValue(dealerHand) > 21:
                    # Dealer has bust
                    break
                input('Press Enter to continue...')
                print('\n\n')

        # Shows the final hands for the player and the dealer
        showHands(playerHand, dealerHand, True)

        playerValue = handValue(playerHand)
        dealerValue = handValue(dealerHand)
        # Evaluate results of the round, win, lose or tie
        if dealerValue > 21:
            print(f'Dealer busts! You win {bet}!')
            chips += bet
        elif (playerValue > 21) or (playerValue < dealerValue):
            print('Unlucky!')
            chips -= bet
        elif playerValue > dealerValue:
            print(f'You won {bet}!')
            chips += bet
        elif playerValue == dealerValue:
            print('Tie! Your bet is returned.')
        updateChipsBalance(current_user['name'], chips)
        input('Press Enter to play again!')
        print('\n\n')


def placeBet(maxBet):
    """
    Lets the player input their bet amount or use 'EXIT' to exit the loop.
    Will only accept valid integers as a bet
    """
    while True:
        # Player inputs their bet amount or has the option to exit the game
        print(f'How much you wanna bet?? (1-{maxBet}, or EXIT)')
        bet = input('> ').upper().strip()
        if bet == 'EXIT':
            exitGame()

        # Loops the function to place a bet if player enters an invalid value
        if not bet.isdecimal():
            continue

        # Places the players bet if the value is a valid integer
        bet = int(bet)
        if 1 <= bet <= maxBet:
            return bet


def cardDeck():
    """
    Returns a list of tuples with the rank and suit for all 52 cards
    in the deck
    """
    deck = []
    for suit in (SPADES, CLUBS, HEARTS, DIAMONDS):
        # Numbered cards between 2 and 10
        for rank in range(2, 11):
            deck.append((str(rank), suit))
        # Jacks, Queens, Kings and Aces
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck


def showHands(playerHand, dealerHand, showDealerHand):
    """
    Shows the players and dealers cards. Hides the dealers first card
    """
    print()
    if showDealerHand:
        print('DEALER:', handValue(dealerHand))
        cardFormat(dealerHand)
    else:
        print('DEALER: ???')
        # Hides the dealers first card and shows the second
        cardFormat([CARDBACK] + dealerHand[1:])

    # Shows the players cards
    print('PLAYER:', handValue(playerHand))
    cardFormat(playerHand)


def handValue(cards):
    """
    Returns the value of the cards. Numbered cards are worth their
    displayed number. Jacks, Queens and Kings are worth 10.
    Aces are worth 11 or 1, an ace will be assigned a value of 11
    unless that would equal more than 21, in which case it will be
    assigned a value of 1
    """
    value = 0
    acesDealt = 0

    # Adds the value for Jacks, Queens and Kings
    for card in cards:
        rank = card[0]
        if rank == 'A':
            acesDealt += 1
        elif rank in ('K', 'Q', 'J'):
            value += 10
        else:
            value += int(rank)

    # Add the value for the Aces
    value += acesDealt
    for i in range(acesDealt):
        if value + 10 <= 21:
            value += 10
    return value


def cardFormat(cards):
    """
    Formats the cards in the terminal using the cards rank and suit
    """
    # A list of empty strings for each row
    rows = ['', '', '', '', '']

    for i, card in enumerate(cards):
        # Top line of each card
        rows[0] += '  __  '
        if card == CARDBACK:
            # Formats the card backs
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            # Formats the card fronts with rank and suit
            rank, suit = card
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, '_'))

    for row in rows:
        print(row)


def playerMove(playerHand, chips):
    """
    Asks the player for their move and returns 'H' for hit, 'S' for
    stand and 'D' for double down
    """
    while True:
        # Displays the available moves to the player
        moves = ['(H)it', '(S)tand']

        # The player can double down on their bet when their cards
        # are first dealt
        if len(playerHand) == 2 and chips > 0:
            moves.append('(D)ouble down')

        # Get the players move
        movePrompt = ', '.join(moves) + '> '
        move = input(movePrompt).upper()
        if move in ('H', 'S'):
            return move
        if move == 'D' and '(D)ouble down' in moves:
            return move


def getChips(chips):
    """
    Function to add 5000 chips to players account that is called once
    their chips get to 0
    """
    updateChipsBalance(current_user['name'], 5000)


def main():
    """
    Function to control the calling of other functions in the file
    """
    homeTitle()
    checkExistingUser()
    gameMenu()


main()

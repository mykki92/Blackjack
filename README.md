# **Blackjack**
Developed by Michael Roberts

<img src="docs/am-i-responsive.png" alt="A screenshot of Am I Responsive representation of the website">

[Link to live site](https://blackjackpython.herokuapp.com/)

## Introduction
Blackjack, also known as 21, is a card game where players attempt to reach a score of 21 — without exceeding it — before the dealer hits 17. You can win if you don't bust and your total is higher than the dealer cards.


## Contents
* [Project Goals](#project-goals)<br>
    * [User Goals](#user-goals)
    * [Site Owner Goals](#site-owner-goals)
* [User Experience](#user-experience)<br>
    * [Target Audience](#target-audience)
    * [User Requirements](#user-requirements)
    * [User Manual](#user-manual)
    * [User Stories](#user-stories)
* [Technical Design](#technical-design)
    * [Data Models](#data-models)
    * [Flowchart](#flowchart)
* [Features](#features)
    * [App Features](#app-features)
    * [Feature Ideas for future development](#feature-ideas-for-future-development)
* [Technologies Used](#technologies-used)
* [Deployment & Local Development](#deployment--local-development)
* [Testing](#testing)
    * [Validation](#validation)
    * [Manual Testing](#manual-testing)
    * [Automated Testing](#automated-testing)
    * [Bugs](#bugs)
* [Credits](#credits)

## Project Goals
### User Goals
* Play a blackjack game and try and win as many chips as possible.
* To understand the instructions and how to play the game.
* To sign up with a new account.
* Log back in to an existing account.

### Site Owner Goals
* To provide users with clear instructions on how to play the game and navigate the program.
* To make sure any user errors are handled and communicated back to the user.

## User Experience
### Target audience
* This game is targeted at people with an interest in Blackjack and people with an interest in computer gaming in general.

### User requirements
* A game that is understandable and works as expected.
* Log-in works as expected and validates user input correctly.
* Game moves and the betting system is clearly communicated and displayed to the user.
* User can quit the game when they want.

### User Manual

### User Stories
#### First Time User
1. As a first time user, I want to set a username and password to sign up for a game account.
2. As a first time user, I want to see clear instructions on how to play the game before starting.
3. As a first time user, I want to have a visual representation of the Blackjack game as I am playing it.
4. As a first time user, I want inputs to work as expected and any errors to be flagged by the program.
5. As a first time user, I want the program to be responsive and provide clear progress and feedback through the steps of the game.

#### Returning User 
7. As a returning user, I want to be able to log in with my existing username and password.
8. As a returning user, I want to be able to continue the game with my previous chips balance.
9. As a returning user, I want to be able skip the instructions if they I'm already familiar with the game.

#### Site Owner
10. As a site owner, I want to ensure that all data entered by the user is validated so as not to break the program or create bad user experience.
11. As a site owner, I want to ensure that all user actions are given feedback in the terminal so that users know what to do next in the game.

## Technical Design
### Flowchart
A flowchart was created using [Lucidchart](https://lucid.app/) to visualise the logic flow of the game.

<details>
    <summary>Flowchart</summary>
    <p>Blackjack game logic:</p>
    <img src="docs/technical-design/flowchart.png" alt="A screenshot of the flowchart of game logic">
</details><br>

### Data Models
* The Google Sheets API was used for user data.
    * This allows user data to be saved so a user can create an account and use it to sign in to the game.

## Features
The website has a single page with several features within the mock python terminal. These features are listed below.
### App Features

### Feature Ideas for Future Development
In future the website could be further developed and improved to offer more games and expand into a general casino-type application, with additional games such as poker, roulette and slot machine games.

## Technologies Used

### Languages Used
Python

### Other Tools Used
* [Git](https://git-scm.com/) was used for version control.
* [GitHub](https://github.com/) was used for saving and storing files.
* [CodeAnywhere](https://app.codeanywhere.com/) was the IDE used for writing and editing code.
* [Heroku](https://id.heroku.com/) was used as the hosting platform for this site.
* [ASCII art generator](https://patorjk.com/software/taag/#p=display&f=Big%20Money-ne&t=Blackjack) was used to generate title text.
* [PEP8 Python Validator](https://pep8ci.herokuapp.com/) Code institute's own Python Linter was used to validate all Python code in this project.
* [Lucidchart](https://lucid.app/) was used to create logic flowchart.
* [amiresponsive](https://ui.dev/amiresponsive) was used to test the website across different screens and generate the picture at the head of this file.


#### 3rd Party Python Libraries Used
* [Gspread / Google Sheets API](https://github.com/burnash/gspread) was used to handle getting/sending data to the google sheet used in the project. This is also not a standard feature of python, so it was necessary to install it for the purposes of this project.
* [Google OAuth 2.0](https://google-auth.readthedocs.io/en/stable/reference/google.oauth2.credentials.html) was used to set up the connection between the project and the developers personal google account. This was necessary because access to a google account via a program is restricted for security reasons.

## Deployment & Local Development
The website was deployed to [Heroku](https://id.heroku.com/) using the following process:
1. Login or create an account at [Heroku](https://dashboard.heroku.com/)
<img src="docs/heroku/heroku1.png">
2. Click on New > Create new app in the top right of the screen.
<img src="docs/heroku/heroku2.png">
3. Add an app name and select location, then click 'create app'.
<img src="docs/heroku/heroku3.png">
4. Under the deploy tab of the next page, select connect to GitHub.
5. Log in to your GitHub account when prompted.
<img src="docs/heroku/heroku4.png">
6. Select the repository that you want to be connected to the Heroku app.
<img src="docs/heroku/heroku5.png">
7. Click on the settings tab.
<img src="docs/heroku/heroku6.png">
8. Scroll down to the config vars section, and add 2 config vars:
    * The first key is CREDS and the value here is the creds.json file that was generated for the google sheets API to work properly.
    * The second key is PORT and the Value is 8000
<img src="docs/heroku/heroku7.png">
9. Once you have set up the config vars, scroll down to buildpacks (still under the settings tab)
10. Add the Python and Node.js buildpacks to your app and make sure that when they are displayed, they appear in the order:
    * Python
    * Node.JS
<img src="docs/heroku/heroku8.png">
11. Navigate back to the settings tab.
12. Select automatic deploys to allow Heroku to build the site with new changes each time changes are pushed to GitHub.
<img src="docs/heroku/heroku9.png">
13. In the 'manual deploy' section beneath this, make sure the branch selected is 'main' and click deploy branch.
<img src="docs/heroku/heroku10.png">
14. The site should now be built and Heroku should provide a url for the built site.

This repository can be forked using the following process:
1. On the repository's page, go to the top-right of the page underneath the dark ribbon.
2. Click on the fork button
3. You can now work on a fork of this project. 

This repository can be cloned using the following process:
1. Go to this repository's page on GitHub.
2. Click on the code button (not the one in the navbar, but the one right above the file list).
3. Select an option, HTTPS, SSH, GitHub CLI.
4. Copy the URL below to your clipboard.
5. Open Git Bash/your IDE terminal.
6. Ensure the directory you are working in is the correct one you want to paste the project into.
7. Type the command '$ git clone'.
8. Paste the URL of the repository after this.
9. Hit enter on your keyboard and the project will be cloned.

## Testing
### Browser Compatability
The site was tested using the following browsers: 
* Google Chrome
* Mozilla Firefox
* Microsoft Edge
* Safari

### Device Testing
The site was tested on the following devices:
* Google Pixel 7
* Samsung Galaxy A7 Lite Tab
* HP Laptop 14
* Apple iMac

### Validation

#### PEP8 Python Validator (Code Institute)
Code institute's own Python Linter [pep8](https://pep8ci.herokuapp.com/) was used to validate all Python code in this project. All code passed with no errors.

<details>
<summary>run.py</summary>
<img src="docs/validation/run-validation.png" alt="A screenshot of pep8 validator confirming run.py code.">
<img src="docs/validation/run-validation-2.png" alt="A screenshot of pep8 validator confirming run.py code.">
</details>

<details>
<summary>gsheet.py</summary>
<img src="docs/validation/gsheet-validation.png" alt="A screenshot of pep8 validator confirming gsheet.py code.">
<img src="docs/validation/gsheet-validation-2.png" alt="A screenshot of pep8 validator confirming gsheet.py code.">
</details>

### Manual Testing
1. As a first time user, I want to set a username and password to sign up for a game account.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Sign-up prompt | When prompted for an existing account at the start of the game, answer 'N' and enter new details | Program creates new user account. | Works as expected. |

<details>
    <summary>Screenshots</summary>
    <img src="docs/user-stories/user-story-1-1.png" alt="A screenshot of the sign up prompt.">
    <img src="docs/user-stories/user-story-1-2.png" alt="A screenshot of the sign up process.">
    <img src="docs/user-stories/user-story-1-3.png" alt="A screenshot of the new account details on gsheet.">
</details>

2. As a first time user, I want to see clear instructions on how to play the game before starting.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Game Menu | When in the main menu, enter 'I' to access instructions. | Program displays instructions and a way to get back to the menu. | Works as expected. |

<details>
    <summary>Screenshots</summary>
    <img src="docs/user-stories/user-story-2-1.png" alt="A screenshot of the game menu.">
    <img src="docs/user-stories/user-story-2-2.png" alt="A screenshot of the instructions.">
</details>

3. As a first time user, I want to have a visual representation of the Blackjack game as I am playing it.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Main Game | Start the game. | Program displays betting function and game cards. | Works as expected. |

<details>
    <summary>Screenshots</summary>
    <img src="docs/user-stories/user-story-3-1.png" alt="A screenshot of the betting function.">
    <img src="docs/user-stories/user-story-3-2.png" alt="A screenshot of the game cards.">
</details>

4. As a first time user, I want inputs to work as expected and any errors to be flagged by the program.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Game Inputs | Enter an incorrect username, password or input. | Program flags the error and input must be entered again. | Works as expected. |

<details>
    <summary>Screenshots</summary>
    <img src="docs/user-stories/user-story-4-1.png" alt="A screenshot of sign in input validation.">
    <img src="docs/user-stories/user-story-4-2.png" alt="A screenshot of sign in input validation.">
    <img src="docs/user-stories/user-story-4-3.png" alt="A screenshot of game menu input validation.">
    <img src="docs/user-stories/user-story-4-4.png" alt="A screenshot of betting input validation.">
    <img src="docs/user-stories/user-story-4-5.png" alt="A screenshot of game move validation.">
</details>


5. As a first time user, I want the program to be responsive and provide clear progress and feedback through the steps of the game.

| **Feature** | **Action** | **Expected Result** | **Actual Result** |
|-------------|------------|---------------------|-------------------|
| Main Game | Play through the game. | See clear feedback and game information and prompts for input. | Works as expected. |

<details>
    <summary>Screenshots</summary>
    <img src="docs/user-stories/user-story-5-1.png" alt="A screenshot of betting prompt.">
    <img src="docs/user-stories/user-story-5-2.png" alt="A screenshot of player move prompt.">
    <img src="docs/user-stories/user-story-5-3.png" alt="A screenshot of dealer move feedback.">
    <img src="docs/user-stories/user-story-5-4.png" alt="A screenshot of game win feedback.">
    <img src="docs/user-stories/user-story-5-5.png" alt="A screenshot of card draw feedback.">
</details>

### Bugs
| Bug Description  | Fix  |
|---|---|
|Between inputting their username and the password input loading, the user could input characters into empty lines, causing issues with login. | Remove time.sleep(1) from between the username and password inputs being loaded. |

| Bug Description  | Fix  |
|---|---|
|Validation issues when using "Press $ to get more chips". | Change input to "Press any button to get more chips". |

| Bug Description  | Fix  |
|---|---|
|When player clicks to get more chips, sometimes the sheet has not updated before the game restarts and the player has the wrong number of chips. | Insert time.sleep(3) in between the getChips and playBlackjack functions to allow time for the sheet to update. |

## Credits
### 3rd Party Python Libraries/Modules
* [Gspread / Google Sheets API](https://github.com/burnash/gspread) was used to handle getting/sending data to the google sheet used in the project.
* [Google OAuth 2.0](https://google-auth.readthedocs.io/en/stable/reference/google.oauth2.credentials.html) was used to set up the connection between the project and the developers personal google account.
* [ASCII art generator](https://patorjk.com/software/taag/#p=display&f=Big%20Money-ne&t=Blackjack) was used to generate title text.

### Acknowledgements
* My Code Institute Mentor Mo Shami for his guidance and advice.
* Code Institute learning modules and tutor support.

################################################################################################
#                               _   _  ___ _____ _____ ____                                    #
#                              | \ | |/ _ \_   _| ____/ ___|                                   #
#                              |  \| | | | || | |  _| \___ \                                   #
#                              | |\  | |_| || | | |___ ___) |                                  #
#                              |_| \_|\___/ |_| |_____|____/                                   #
#                                                                                              #
#                                                                                              #
# Key Sprint: How fast are your fingers?                                                       #
# Created by Matthew Rosca-Halmagean & Rachel Connelly                                         #
#                                                                                              #
# All of code written in this program is licensed under the MIT License.                       #
#                                                                                              #
# Code has been been written and tested for OS X Yosemite Version 10.10.3 using Python 2.7.10. #
# We do not provide support for any platforms other than the ones listed above.                #
#                                                                                              #
# Please read the README.txt file included in your download for more information.              #
#                                                                                              #
################################################################################################


# Import modules that will be referenced in the code
from sys import argv
import time
import os
import string
import random
import getch
import getpass
import subprocess


# Version number
__version__ = '0.1.0'


# Define HighScore file as HighScore.txt
HighScore = 'HighScore.txt'

# Global variables
score = 0
correct = 0
incorrect = 0

# Get name of user
account_user = getpass.getuser()

# Define path to KeySprint directory
source = os.getcwd()

# Check files in source directory
for files in source:
    # Check to find HighScore.txt file
    if not os.path.exists(source + '/HighScore.txt'):
        # Create HighScore.txt file
        create = open(HighScore, 'a')

        # Write current high score as 0
        create.write('0')

        # Skip one line in the file
        create.write('\n')

        # Set high score user as null
        create.write('null')

        # Close HighScore.txt file
        create.close()

# Define audio paths
correct_audio = source + '/Sounds/correct.wav'
incorrect_audio = source + '/Sounds/incorrect.wav'
intro_audio = source + '/Sounds/intro.wav'
select_audio = source + '/Sounds/select.wav'


# Prompt for user's name
userName = raw_input("\nFirst, please enter your name.\n")
print("\nWelcome, " + userName + "!")

# Play intro sound
subprocess.call(["afplay", intro_audio])


# Start menu that begins the game
def start():
    # Directions and "How to Play"
    print("\nIn this game, the program is going to give you a key to press on your keyboard.")
    print("Once you've done that, you're going to be given another key to press.")
    print("Your goal is to get as many keys pressed correctly as you can in 10 seconds.")

    # Wait two seconds
    time.sleep(2)

    # Listens for key press
    # Only proceed once the user presses a key
    os.system('read -s -n 1 -p "Press any key to continue.\n"')

    # Play selection sound
    subprocess.call(["afplay", select_audio])

    # Bring user to countdown function
    countdown()


# Countdown timer
# Starts game immediately afterwards
def countdown():
    # Calls global variables
    global score, correct, incorrect

    # Resets global variables
    score = 0
    correct = 0
    incorrect = 0

    # Countdown from five
    # Wait 0.5 seconds between number
    print("\n5")
    time.sleep(0.5)
    print("4")
    time.sleep(0.5)
    print("3")
    time.sleep(0.5)
    print("2")
    time.sleep(0.5)
    print("1")

    # Finish countdown
    print("GO!\n")

    # Bring user to core function
    core()


# Contains all game functionality
def core():
    # Calls global variables
    global score, correct, incorrect

    # Define start time
    begin = time.time()

    # Loops until 10 seconds are up
    # Subtracts start time from current time
    # Continue loop while less than 10
    while time.time() - begin < 10:

        # Select a random character
        task = random.choice(string.ascii_uppercase)

        # Print random character
        print task

        # Get character that user presses
        k1 = getch.getch()

        # Convert letter to uppercase
        k2 = k1.upper()

        # Compare user character to random character
        # Characters match
        if k2 == task:
            # Add six points to user score
            score += 6

            # Add one to correct total
            correct += 1

        # Compare user character to random character
        # Characters do not match
        if k2 != task:
            # Subtract three points from user score
            score -= 3

            # Add one to incorrect total
            incorrect += 1

    # Bring users to scores function
    scores()


# Score checking and high scores
def scores():
    # Calls global variables
    global score, correct, incorrect

    # Convert correct and incorrect totals
    # From integer to string
    correct = str(correct)
    incorrect = str(incorrect)

    # Open HighScore.txt file
    target = open(HighScore)

    # Read file by line individually
    lines = target.readlines()

    # Pull high score from line one
    # Define as high score variable
    high = lines[0]

    # Convert high score to integer
    high = int(high)

    # Pull high score user from line two
    # Define as high score user variable
    holder = lines[1]

    # Close HighScore.txt file
    target.close()

    # Check if user score beats high score
    if score > high:
        # Convert user score to string
        score = str(score)

        # Open HighScore.txt file
        target = open(HighScore, 'w')

        # Wipe HighScore.txt file
        target.truncate()

        # Add user score to line one
        # User score is the new high score
        target.write(score)

        # Skip one line in the file
        target.write("\n")

        # Add user name to line two
        # User name is the new high score name
        target.write(userName)

        # Close HighScore.txt file
        target.close()

        # Inform user they beat the high score
        # Inform user the score they received
        # Inform user how many correct and incorrect
        print("\nCongratulations, " + userName + "! You got the new high score!\n\nYour score was " + score + ".\n")
        print("You got " + correct + " correct and " + incorrect + " incorrect.\n")

        # Play correct audio
        subprocess.call(["afplay", correct_audio])

        # Wait 0.5 seconds
        time.sleep(.5)

        # Bring user to retry function
        retry()

    # Check if user score is equal to high score
    if score == high:
        # Convert user score to string
        score = str(score)

        # Inform user they tied the high score
        # Inform user the score they received
        # Inform user how many correct and incorrect
        print("\nYou met the high score, but you did not exceed it.\n\nYour score was " + score + ".\n")
        print("You got " + correct + " correct and " + incorrect + " incorrect.\n")

        # Play incorrect audio
        subprocess.call(["afplay", incorrect_audio])

        # Wait 0.5 seconds
        time.sleep(.5)

        # Bring user to retry function
        retry()

    # Check if user score is less than high score
    if score < high:
        # Convert high score to string
        high = str(high)

        # Convert user score to string
        score = str(score)

        # Inform user they did not beat the high score
        # Inform user the score they received
        # Inform user how many correct and incorrect
        # Inform user the high score and high score user
        print("\nSorry, you did not get the high score.\n\nYour score was " + score + ".\n")
        print("You got " + correct + " correct and " + incorrect + " incorrect.\n")
        print("The current high score is " + high + " and is held by " + holder + ". Better luck next time!\n")

        # Play incorrect audio
        subprocess.call(["afplay", incorrect_audio])

        # Wait 0.5 seconds
        time.sleep(.5)

        # Bring user to retry function
        retry()

    # Bring user to retry function
    retry()


# Prompts user to restart or quit
def retry():
    # Ask user to play again
    over = raw_input("\nWould you like to play again?\n")

    # Convert user input to lowercase
    over = over.lower()

    # If user input is yes
    if over == "yes":
        # Print restart message
        print("\nRestarting Key Sprint...")

        # Wait 0.5 seconds
        time.sleep(.5)

        # Bring user to countdown function
        countdown()

    # If user input is no
    if over == "no":
        # Print quit message
        print("\nSee you next time!\n")

        # Quit game.py
        quit()

    # If user input is unknown
    else:
        # Print help message
        print("\nPlease reply with \"yes\" or \"no\".\n")

        # Restart retry function
        retry()

# Call start function
# Begin game
start()

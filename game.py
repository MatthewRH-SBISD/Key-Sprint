import time
from sys import argv
script, HighScore.txt = argv

# start menu
print("Welcome ...")
userName = raw_input("First, please enter your name.")

def startGame():
    print("In this game, the program is going to give you a key to press on your keyboard.")
    print("Once you've done that, you're going to be given another key to press.")
    print("Your goal is to get as many keys pressed correctly as you can in 60 seconds.")
    beginPlay = input("Would you like to play the game?")
    beginPlay = beginPlay.lower()
    if beginPlay == "yes":
        print("Good luck!")
        time.sleep(.5)
        nextScreen = gamePlay
    elif beginPlay == "no":
        print("See you next time!")
        nextScreen = quit()
    else:
        print("Please reply with \"yes\" or \"no\".")
        beginPlay()


# play again
def playAgain():
    gameOver = input("Would you like to play again?")
    gameOver = gameOver.lower()
    if gameOver == "yes":
        print("Good luck!")
        time.sleep(.5)
        nextScreen = startGame
    elif gameOver == "no":
        print("See you next time!")
    else:
        print("Please reply with \"yes\" or \"no\".")
        gameOver()


# high score

def scoreBoard():
    target = open(HighScore.txt)
    target.truncate()
    currentHighScore = target.read(line1)
    currentHighScore = int(currentHighScore)
    if userScore > currentHighScore:
        target.write(line1)
        print("Congratulations! You got the new high score!")
        time.sleep(.5)
        playAgain()
    elif userScore == currentHighScore:
        print("You met the high score, but you did not exceed it.")
        time.sleep(.5)
        playAgain()
    else:
        print("Sorry, you did not get the high score.")
        print("The current high score is: ", currentHighScore)
        time.sleep(.5)
        playAgain()
    target.close()


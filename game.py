# finish game

def finishGame():
    gameOver = input("Would you like to play again?")
    gameOver = gameOver.lower()
    if gameOver == "yes":
        nextScreen = startGame
    elif gameOver == "no":
        nextScreen = quit()
    else:
        print("Please reply with yes or no.")
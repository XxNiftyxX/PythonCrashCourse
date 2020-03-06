# -------------------------------------------------------
# Project: Guess the number between a range.
# Author/Date: Darren Kunz, Feb 19, 2020

# Goals: Learn basics of input, display, and variables
# Challenges faced: learning random number generation, string and integers wouldn't concatenate without casting,
# variables not being changable by function

# Steps: Get number from user. Generate number from 0 - user number. Ask for guess. Keep track of how many guesses.
#       Give option for hints, keep track of hints/guesses. Loop if guess is wrong. Exit program when guess is correct
#       or they give up. experiment with gui.
# --------------------------------------------------------
import random  # import library for random numbers

playAgain = True
while playAgain is True:
    topRange = input("Enter a number: ")  # I am unsure at this point how to handle incorrect input

    correctNumber = random.randint(0, int(topRange))


    def evaluate():
        global totalGuesses     # necessary to change variables outside of this function
        global totalHints

        if guess == "exit":
            print("Exiting Program!" + str(correctNumber) + " " + topRange)
            global playAgain
            playAgain = False
            return True
        if guess == "hint":

            totalHints += 1
            hint = random.randint(0, int(topRange))
            hint2 = random.randint(0, int(topRange))
            if abs((hint2-correctNumber)) < abs(hint-correctNumber):   # finds which of the two numbers is closer to ans
                hint = hint2                                # in this case hint2 is closer than hint and overrides
            print("You should guess a number close to " + str(hint))
            return False
        totalGuesses += 1
        if guess == str(correctNumber):
            print(guess + " is Correct! It only took you " + str(totalGuesses) + " guesses and " +
                  str(totalHints) + " hints!")

            if input("Would you like to play again? Type 'exit' to exit or any key to continue.") == "exit":
                playAgain = False
            return True
        else:
            print(guess + " is incorrect! ")
            if int(guess) < correctNumber:
                print("Try guessing a number higher than " + guess)
            else:
                print("Try guessing a number lower than " + guess)
            return False


    totalGuesses = 0  # initialize starting variables
    totalHints = 0
    correct = False  # To exit while loop we must get a correct guess to change variable to True

    while correct is False:
        guess = input("Guess a number between 0 and " + topRange + " (type 'hint' for hints or 'exit' to exit): ")
        correct = evaluate()




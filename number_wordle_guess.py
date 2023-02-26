import random

def main():

    guesses = 0
    print("\n-------------------------------------")
    difficulty = input("\nEnter difficulty ['Easy' or 'Hard']: ").upper()

    if(difficulty == "EASY"): guesses = 9
    elif(difficulty == "HARD"): guesses = 5
    else:
        print("\nInvalid difficulty.")
        print("Run the program again to retry.")
        guesses = -1

    num = random.randrange(2, 49)

    if(guesses == -1):
        print("")
    else:
        print("\nI am thinking of a number between 1 and 50, inclusive.")

        print("\nEnter", guesses, "guesses: ")
        print("")

        result = "\nSorry, you did not guess correctly."

        while(guesses > 0):
            guess = int(input())
            guesses -= 1

            if(guess > num):
                print("Too high")
            elif(guess < num):
                print("Too low")
            else:
                result = ("\nYou guessed correctly!")
                guesses = 0

        print(result)
        reset = input("\nDo you wish to play again? ['Yes' or 'No']: ").upper()

        if(reset == "YES"):
            main()
        else:
            exit()

main()
            

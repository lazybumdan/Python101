import random

def guess_the_number():
    while True:
        number = int(input("Guess a number between 1 and 10: "))
        guessed = random.randint(1, 10)
        if number == guessed:
            print("Congratulations! You guessed it!")
            break
        else:
            retry = input(f"Sorry, that's wrong. The correct number is {guessed}. Would you like to try again?(Y/N)")
            if retry == "Y" or retry == "y":
                continue
            else:
                break



guess_the_number()

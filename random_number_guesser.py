import random

def guess_the_number():
    while True:
        user_number = int(input("Guess a number between 1 and 10: "))
        actual_number = random.randint(1, 10)
        if user_number >= 10 or user_number < 1:
            print("Please enter a number between 1 and 10")
        elif user_number == actual_number:
            print("Congratulations! You guessed it!")
            break
        else:
            retry = input(f"Sorry, that's wrong. The correct number is {actual_number}. Would you like to try again?(Y/N)")
            if retry == "Y" or retry == "y":
                continue
            else:
                break



guess_the_number()

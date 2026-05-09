import random

def roulette():
    colour = input("Please select either Black or Red: ")
    number = int(input("Please select a number from 1 to 36: "))
    if number > 36 or number < 1:
        print("Please select a number from 1 to 36")
    actual_colour = random.choice(['Black', 'Red'])
    actual_number = random.randint(1, 36)
    if actual_colour == colour:
        print("You got the colour right!")
    if actual_number == number:
        print("You got the number right!")
    print(f"The actual colour is {actual_colour}. The actual number is {actual_number}.")

def main():
    print("Welcome to Daniel's Casino!")
    game_selection = input("Which game would you like to play? Roulette or Blackjack? ")
    if game_selection == "Roulette":
        roulette()
    elif game_selection == "Blackjack":
        blackjack()
    else:
        print("Invalid input. Please try again.")

main()

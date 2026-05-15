# A very simple python calculator
print("Welcome to Daniel's calculator! \n'It can add, subtract, multiply and divide any number!")
x = float(input("What is your first number?: "))
y = float(input("What is your second number?: "))

def addition():
    print("The sum is: ", x + y)

def subtraction():
    print("The subtraction is: ", x - y)

def multiply():
    print("The multiplication is: ", x * y)

def division():
    print("The division is: ", x / y)

def squaring():
    print("The square is: ", x ** 2)

def square_root():
    print("The square root of is: ", x ** (1 / 2))

def main():
    choice = input(" 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5. Squaring \n 6. Square Root \n Please enter your choice 1-6:  ")
    if choice == "1":
        addition()
    elif choice == "2":
        subtraction()
    elif choice == "3":
        multiply()
    elif choice == "4":
        division()
    elif choice == "5":
        squaring()
    elif choice == "6":
        square_root()


if __name__ == "__main__":
    main()

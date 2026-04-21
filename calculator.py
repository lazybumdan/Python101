# A very simple python calculator
print("Welcome to Daniel's calculator! \n'It can add, subtract, multiply and divide any number!")
def calculator():
    while True:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operator = input("Enter a operator, the options are +,-,*,/,%,**: ")
        if operator == "+":
            ans = (num1 + num2)
            print(ans)
        elif operator == "-":
            ans = (num1 - num2)
            print(ans)
        elif operator == "*":
            ans = (num1 * num2)
            print(ans)
        elif operator == "/":
            ans = (num1 / num2)
            print(ans)
        elif operator == "%":
            ans = (num1 % num2)
            print(ans)
        elif operator == "**":
            ans = (num1 ** num2)
            print(ans)
        rounded = input("Do you want to round the calculation? (y/n): ")
        if rounded == "y":
            print(int(ans))
        prompt = input("Would you like to continue? (y/n): ")
        if prompt == "y":
            continue
        else:
            break
            
calculator()

The goal of the calculator is to allow users to do simple addition, subtraction, multiplication and division aswell as giving them the
option to round the output number and also allowing them to either continue doing more calculations or stopping the code effectively 
turning it off.
# A little explaination on the code written above 


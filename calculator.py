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

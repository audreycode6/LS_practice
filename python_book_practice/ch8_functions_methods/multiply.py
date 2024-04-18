# a program that uses a multiply function to multiply two numbers and returns the result.
# Ask the user to enter the two numbers,
# then output the numbers and result as a simple equation.


def multiply():
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    multiplier = number1 * number2
    print(f"{number1} * {number2} = {multiplier}")


multiply()

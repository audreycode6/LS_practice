# multiply.py adjusted for reusability, takes argument
def multiply(left, right):
    return left * right


def number_prompt(prompt):
    number_input = input(prompt)
    return float(number_input)


number1 = number_prompt("Enter first number: ")
number2 = number_prompt("Enter second number: ")
multiplier = multiply(number1, number2)
print(f"{number1} * {number2} = {multiplier}")

# Examine the function invocation below. Write the function multiply, such that it accepts two arguments and returns the product of its arguments. You may assume that the function arguments will always be numbers.

# multiply(12, 4)     # 48

num1 = int(input("Enter an integer: "))
num2 = int(input("Enter an integer: "))


def multiply(num1, num2):
    return num1 * num2


print(multiply(num1, num2))  # wrap function call with print() to output result


# OR you can just create function and manually add arguments when calling
def multiply2(a, b):
    return a * b


print(multiply2(6, 2))

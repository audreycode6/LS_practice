# Write a function that computes and returns the factorial of a number
# by using a for or while loop.
# The factorial of a positive integer n, signified by n!,
# is defined as the product of all integers between 1 and n, inclusive:

n = int(
    input(
        "Enter a postive integer: ",
    )
)


def factorial(n):
    index = 1
    factors = 1
    while index <= n:
        result = index * factors
        factors = result  # keep going through multipling the numbers of 1-n
        index += 1  # update index so it will stop after multiplying to n
    return result


show_return = factorial(n)
print(f"{show_return} is the factorial of {n}!")

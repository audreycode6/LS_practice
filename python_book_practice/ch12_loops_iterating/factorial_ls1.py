n = int(
    input(
        "Enter a postive integer: ",
    )
)


def factorial(n):
    product = 1
    while n > 0:
        product *= n
        n -= 1
    return product


factorial_return = factorial(n)
print(f"{factorial_return} is the factorial of {n}!")

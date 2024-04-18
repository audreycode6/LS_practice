n = int(
    input(
        "Enter a postive integer: ",
    )
)


def factorial(n):
    product = 1
    for number in range(n, 0, -1):
        product *= number
    return product


show_factorial = factorial(n)
print(f"{show_factorial} is the factorial of {n}")

# Write a function that takes a single integer argument and
# prints a message that describes whether:
# the value is between 0 and 50 (inclusive)
# the value is between 51 and 100 (inclusive)
# the value is greater than 100
# the value is less than 0
integer = int(input("Enter a whole number: "))


def integer_range(integer):
    if integer >= 0 and integer <= 50:
        print(f"{integer} is between 0 and 50")
    elif integer >= 51 and integer <= 100:
        print(f"{integer} is between 51 and 100")
    elif integer >= 100:
        print(f"{integer} is greater than 100")
    else:
        print(f"{integer} is less than 0")


integer_range(integer)

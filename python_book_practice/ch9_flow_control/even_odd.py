# function, even_or_odd, that determines whether its argument is an even or odd number.
# If it's even, the function should print 'even';
# otherwise, it should print 'odd'. Assume the argument is always an integer.
number = int(input("Enter a whole number: "))


def even_or_odd(number):
    even = number % 2  # could just put this in if statement rather than variable
    if even == 0:
        print(f"{number} is even")
    else:
        print(f"{number} is odd")


even_or_odd(number)

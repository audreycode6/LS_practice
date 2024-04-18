# When the user inputs 10, we expect the program to print The result is 50!,
# but that's not the output we see. Why not?


# def multiply_by_five(n):
#     return n * 5


# print("Hello! Which number would you like to multiply by 5?")
# number = int(input())
# print(f"The result is {multiply_by_five(number)}!")
# registered as a string so string just get multipled so number entered at input is just multipled as a string ie. stringnumber concatenated 5 times
# ex: number = 10, prints 1010101010 (5 10's)


# personally would rewrite:


def multiply_by_5(n):
    return f"The result is {n * 5}!"


n = int(input("Enter a number to multiply by 5: "))
print(multiply_by_5(n))

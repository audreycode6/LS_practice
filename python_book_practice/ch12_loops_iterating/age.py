# asks the user to enter their age, then calculates and
# reports the future age 10, 20, 30, and 40 years from now.
# use a for loop to display the future ages.

age = int(
    input(
        "How old are you? ",
    )
)
print(f"You are {age} years old!")

multiplier = [10, 20, 30, 40]
ages = []

for number in multiplier:
    calculate = age + number
    ages.append(calculate)
    print(f"In {number} years, you will be {calculate} year old!")

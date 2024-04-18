age = int(
    input(
        "How old are you? ",
    )
)
print(f"You are {age} years old!")
print()

for years in range(10, 50, 10):
    print(f"In {years} years, you will be {age + years} years old!")

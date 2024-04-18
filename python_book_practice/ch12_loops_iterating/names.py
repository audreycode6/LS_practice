names = ["Tiger", "Goose", "Audrey", "Andrei"]
upper_names = []

for name in names:
    if name != "Goose":
        upper_name = name.upper()
        upper_names.append(upper_name)

print(upper_names)


for char in "Audrey Theriault":
    print(char)

for word in "You silly little Goose!".split():
    print(word)

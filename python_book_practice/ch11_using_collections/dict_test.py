pets = {
    "Cat": "Meow",
    "Dog": "Bark",
    "Bird": "Tweet",
}
print(pets["Dog"])  # since known don't need to use get
print(pets.get("Dog"))  # better practice if wasn't sure Dog was a key
print(pets.get("Lizard"))  # not there == default None
print(pets.get("Lizard", "<silence>"))  # default value if non existing "<silence>"

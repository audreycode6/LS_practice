# Use a for loop to iterate over the numbers dictionary and
# print each element's key/value pair.

numbers = {
    "high": 100,
    "medium": 50,
    "low": 10,
}

for number in numbers:
    print(f"A {number} number is {numbers[number]}.")
    # Output:
    # A high number is 100.
    # A medium number is 50.
    # A low number is 10.

print()
# OR use dict.items() method
for key, value in numbers.items():
    print(f"A {key} number is {value}.")

# you can iterate over dictionary key/value pairs using the
# dict.items method within a for loop. dict.items returns
# an iterable of tuples, where each tuple contains a key/value pair.
# You can extract the key and value from the tuple by using key,
# value where you normally place a single variable.

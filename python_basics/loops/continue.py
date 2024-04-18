# Write a for loop that iterates over the elements of the list cities and
# prints the length of each string.
# If the element is None, use the continue statement to skip forward
# to the next iteration without printing anything.
cities = [
    "Istanbul",
    "Los Angeles",
    "Tokyo",
    None,
    "Vienna",
    None,
    "London",
    "Beijing",
    None,
]
for city in cities:
    if city == None:
        continue
    # continue statement effectively skips the print statement for None values,
    # making an else unnecessary in this context.
    print(len(city))

    # OR pretty print:
    # print(f"Length of the word '{city}' is: {len(city)}!")

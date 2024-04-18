# Write a function that returns the first element of a list provided
# as an argument. Be sure to handle the case where the input list is empty.


def first(list):
    if list:  # if list is not empty
        return list[0]
    else:  # if empty list, let user know
        return "Empty list, no first element to return!"


# TEST
print(first(["Earth", "Moon", "Mars"]))  # Earth
print(first([]))  # Empty list, no first element to return!
print(first("pretzel"))  # p

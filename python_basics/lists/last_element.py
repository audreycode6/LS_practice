# Write a function that returns the last element of a list provided as
# an argument.
# Be sure to handle the case where the input list is empty.


def last(list):
    if list:
        return list[-1]  # last element in list == [-1]
    else:
        return "Empty list, no last element to return."


# TEST
print(last(["Earth", "Moon", "Mars"]))  # Mars
print(last([]))  # Empty list, no last element to return.

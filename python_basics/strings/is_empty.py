# Write a function that checks whether a string is empty or not.
def is_empty(string):
    # return len(string) == 0  # true if empty/ else false

    # OR

    return string == ""  # true if empty/ else false

    # OR

    # return not string

    # OR (more code than needed but works)

    # if string == "":
    #     return True
    # else:
    #     return False


# TEST
print(is_empty("mars"))  # False
print(is_empty("  "))  # False
print(is_empty(""))  # True
print(is_empty("!"))  # False

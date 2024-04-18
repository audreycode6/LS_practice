# Write an is_empty_or_blank function to determine whether a string is
# either empty or consists entirely of spaces.
def is_empty_or_blank(string):
    return string is "" or string.isspace()


# TEST
print(is_empty_or_blank("mars"))  # False
print(is_empty_or_blank("  "))  # True
print(is_empty_or_blank(""))  # True
print(is_empty_or_blank("!"))  # False
print(is_empty_or_blank("\n"))  # True

# how can you check if a variable holds a value that is a list?
# Given two variables, verify whether the values they hold are lists.

# TEST variables
some_value1 = [0, 1, 0, 0, 1]
some_value2 = "I leave you my Kingdom, take good care of it."
some_value3 = ["hi", "bye"]
some_value4 = 12


def is_list(variable1, variable2):
    # use type() function to store type of argument
    variable1_type = type(variable1)
    variable2_type = type(variable2)

    # conditions for return:
    # both are lists
    if variable1_type is list and variable2_type is list:  # if both
        return "Both variables are lists!"
    # only 1 is list (1st or 2nd variable)
    elif variable1_type is list:
        return f"Only the 1st variable is a list: {variable1}"
    elif variable2_type is list:
        return f"Only the 2nd variable is a list: {variable2}"
    # both are not lists; tell user what type it is
    else:
        return f"No lists found. 1st variable is a: {variable1_type} and 2nd variable is a: {variable2_type}."


# TEST
print(is_list(some_value1, some_value2))  # Only the 1st variable is a list: {variable1}
print(is_list(some_value2, some_value3))  # Only the 2nd variable is a list: {variable2}
print(is_list(some_value3, some_value4))  # Only the 1st variable is a list: {variable1}
print(is_list(some_value1, some_value3))  # Both variables are lists!
print(is_list(some_value2, some_value4))
# No lists found. 1st variable is a: {variable1_type} and 2nd variable is a: {variable2_type}

# OR isinstance() function does that
print(isinstance(some_value1, list))  # True
print(isinstance(some_value2, list))  # False
print(isinstance(some_value3, list))  # True
print(isinstance(some_value4, list))  # False

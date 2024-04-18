# a find_integers function that returns
# a list of all the integers from my_tuple:


# list comprehension
def find_integers(collection):
    return [object for object in collection if type(object) is int]


my_tuple = (1, "a", "1", 3, [7], 3.1415, -4, None, {1, 2, 3}, False)
integers = find_integers(my_tuple)
print(integers)  # [1, 3, -4]

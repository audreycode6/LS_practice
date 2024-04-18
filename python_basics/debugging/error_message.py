# What errors does it raise for the given examples and
# what exactly do the error messages mean?
def find_first_nonzero_among(numbers):
    for n in numbers:
        if n != 0:
            return n


# ERRORS:
# find_first_nonzero_among(0, 0, 1, 0, 2, 0)
# find_first_nonzero_among(1)


fix1 = [0, 0, 1, 0, 2, 0]
print(find_first_nonzero_among(fix1))  # (0, 0, 1, 0, 2, 0)
# TypeError: find_first_nonzero_among() takes 1 positional argument but 6 were given
# the argument should be a variable for a list/collection, not just a tuple of all data

fix2 = (1, 3)
print(find_first_nonzero_among(fix2))  # (1)
# TypeError: 'int' object is not iterable
# 1 is not a collection to iterate over
# for loop expects a collection of elements to loop through

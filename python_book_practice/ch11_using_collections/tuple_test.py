# Write Python code to create a new tuple from (1, 2, 3, 4, 5).
# The new tuple should be in reverse order from the original.
# It should also exclude the first and last members of the original.
# The result should be the tuple (4, 3, 2).

tuple1 = (1, 2, 3, 4, 5)

temp_list = list(tuple1)  # convert tuple to list so it can be mutable

reverse = temp_list[::-1]  # reverse

remove1st_last = reverse[1:4]  # slice so we remove 1st and last element

print(tuple(remove1st_last))  # revert to tuple and output

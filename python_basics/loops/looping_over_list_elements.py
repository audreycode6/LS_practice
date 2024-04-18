# Using the code below as a starting point,
# write a while loop that prints the elements of lst at each index
# and terminates after printing the last element of the list.
lst = [1, 3, 7, 15]
index = 0
while index < len(lst):  # OR while index <= len(lst) - 1:
    print(lst[index])
    index += 1

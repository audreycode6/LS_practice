# We have a grocery list. As we check off items on that list,
# we want to remove them from the list.

# Write code that removes the items from grocery_list, one by one,
# until it is empty. If you print the elements you remove,
# the expected behavior would look as follows.

grocery_list = ["paprika", "tofu", "garlic", "quinoa", "carrots", "broccoli", "hummus"]

print(grocery_list)  # print original list

while len(grocery_list) > 0:
    print(grocery_list[0])  # print what will be removed (1 grocery at a time)
    grocery_list.pop(0)  # remove item from list starting with first item
    # .pop alters the list


print(grocery_list)  # [] --> should be empty when while loop is done
# Expected output
# paprika
# tofu
# garlic
# quinoa
# carrots
# broccoli
# hummus
# []

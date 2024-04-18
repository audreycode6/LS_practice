# We have a grocery list. As we check off items on that list,
# we want to remove them from the list.

# Write code that removes the items from grocery_list, one by one,
# until it is empty.

grocery_list = ["paprika", "tofu", "garlic", "quinoa", "carrots", "broccoli", "hummus"]

count = 1
while count < len(grocery_list) + 1:
    print(grocery_list[count : len(grocery_list)])  # new slice to print list,
    # changing slice start to count index; i.e removing 1 item from list at a time
    count += 1
print("You have checked off all your groceries from your grocery list!")

# OUTPUT:
# ['tofu', 'garlic', 'quinoa', 'carrots', 'broccoli', 'hummus']
# ['garlic', 'quinoa', 'carrots', 'broccoli', 'hummus']
# ['quinoa', 'carrots', 'broccoli', 'hummus']
# ['carrots', 'broccoli', 'hummus']
# ['broccoli', 'hummus']
# ['hummus']
# []
# You have checked off all your groceries from your grocery list!
print()

# OR list.pop(index) method removes & returns the element at the specified index from the list.
grocery_list2 = ["paprika", "tofu", "garlic", "quinoa", "carrots", "broccoli", "hummus"]

# use range(0, len(grocery_list2)) to safely pop items from grocery_list2 without affecting the loop's behavior.
for grocery in range(0, len(grocery_list2)):
    checked_item = grocery_list2.pop(0)
    print(checked_item)
print(grocery_list2)
print("You have checked off all your groceries from your grocery list!")

# OUTPUT:
# paprika
# tofu
# garlic
# quinoa
# carrots
# broccoli
# hummus
# []
# You have checked off all your groceries from your grocery list!

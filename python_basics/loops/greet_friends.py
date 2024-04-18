# Your friends just showed up! Given the following list of names,
# use a for loop to greet each friend individually.
friends = ["Sarah", "John", "Hannah", "Dave"]
# common practice to use plural (friends) for object that is being iterated through
# and nonpural (friend) to reference the elements in object
for friend in friends:
    print(f"Hello, {friend}!")

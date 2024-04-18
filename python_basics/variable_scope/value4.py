a = 1


def my_function():
    print(a)


my_function()


# it would print 1. in my_function() it is not altering the variable a,
# it is just calling for it to be printed so when it's not found locally
# it would find a initialized to 1 outside its scope.

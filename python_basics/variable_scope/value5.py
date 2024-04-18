a = 1


def my_function():
    print(a)
    a = 2  # python sees that a is getting ressgined so it views a as local variable
    # need to define first a variable to global or new local a variable


my_function()

# Python detects that a is being assigned within the my_function function
# and therefore treats it as a local variable.
# However, since we are trying to print the local a variable's value before
# it has been assigned a value, we get an error.

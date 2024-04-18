# What will the following code do and why?
# Don't run it until you have tried to answer.

a = 1


def my_function():
    print(a)
    a = 2


my_function()
# raises error bc it sees a is a variable in my_function,
# so ignores the outer a =1
# need to set a =2 before print(a)

# What will the following code do and why?
# Don't run it until you have tried to answer.


x = 10


def my_function():
    x = x + 5
    print(x)


my_function()
# raises Error, bc x is not defined inside my_function,
# need to set outside x as global varialbe if want to use the x= 10 value
# or set new local variable and define in my_fucntion

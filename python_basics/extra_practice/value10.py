# What will the following code do and why?
# Don't run it until you have tried to answer.

b = [1, 2, 3]


def my_function():
    b[0] = 10


my_function()
print(b)
# it would print b's value:  [10,2,3]
# bc my_function is called it reassigns the values of b's 0 index
# which changes b from [1, 2, 3] to [10, 2, 3]
print('hello')

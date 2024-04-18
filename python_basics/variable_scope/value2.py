x = 10


def my_function():
    global x  #: would store x
    x = x + 5
    print(x)


my_function()
# test to see what x's value is outside of functions (it is altered/reassigned)
print(x)


# first answer (WRONG): It would print 15.
# first x is initialized to 10 globally then when my_function is called
# it goes through the body: x = x +5, I.e 10 + 5 = 15;
# x gets reassigned to 15 and when it calls print(x), it would print 15.

# 2nd answer: problem is that in my_function x is being reassigned
# but bc it is from outside scope,
# we can't alter it without making x a global variable;
# when we are modifying a variable outside of the functions scope it needs to be global


# ls: Python assumes that x is a local variable since we're assigning it
# inside the function. However, since it is uninitialized, we get an error.
# If we wanted to modify the global x, we would need to use the global keyword.

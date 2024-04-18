# What will the following code do and why?
# Don't run it until you have tried to answer.

a = 7


def my_function(b):
    b += 10


my_function(a)
print(a)
# it wouldprint 7 and the function would return 17
# in my_function a is sent as an arg but it uses b+= 10 which means b = (a/7) + 10
# == b =17
# a never gets changed since it just an argument passed through

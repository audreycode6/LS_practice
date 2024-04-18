a = 7


def my_function(b):
    b += 10


my_function(a)
print(a)
#  Chatgpt answer: The code will actually output 7.

# In Python, integers are immutable, which means that when you pass an integer
# to a function, you're passing a copy of its value, not a reference to the
# original variable. So, when a is passed to my_function, a copy of the value
# 7 is passed and stored in b. When b is incremented by 10,
# it only affects the local variable b, not the global variable a.

# Your understanding is on the right track, but the key point about
# immutability of integers in Python was missed.

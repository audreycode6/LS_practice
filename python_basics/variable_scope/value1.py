if True:
    my_value = 20

print(my_value)

# 1st answer: Would print None, since no truthy statement (?) -WRONG ANSWER

# it would print 20 bc variables in inner scope can be accessed outside of scope.
# if True statement has True which is a truthy value,
# which initalizes our variable and can then be accessed when called to print


if False:
    my_new_value = 42

# print(my_new_value) # ERROR: my_new_value is not defined


# LS answer: In this case, Python will raise a NameError.
# While my_new_value is in scope,
# it hasn't been set to a value, so remains undefined.
# if False: has False == falsy statement
# so variable is not initialized in global scope and cannot be printed below

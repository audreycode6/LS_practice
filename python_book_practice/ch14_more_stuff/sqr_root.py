# Use the sqrt function from the math library to write
# some code that outputs the square root of 37.
# Try to write the code in three different ways.

# 1. import module and then use module function
import math

print(math.sqrt(37))

# 2. from ; import function from module
from math import sqrt

print(sqrt(37))

# 3. as; import module /functions with alias'
import math as m

print(m.sqrt(37))

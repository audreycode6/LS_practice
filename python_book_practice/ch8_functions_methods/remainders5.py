def remainders_5(numbers):
    return [number % 5 for number in numbers]


# lists to check
numbers_1 = [
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
]  # [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0] # False
numbers_2 = [1, 2, 3, 4, 6, 7, 8, 9]  # [1, 2, 3, 4, 1, 2, 3, 4] #True
numbers_3 = [0, 5, 10]  # [0, 0, 0] #False
numbers_4 = []  # True

# use any();
# False == there are some/all numbers not divisible evenly by 5
# True == some numbers are evenly divisible by 5
print(all(remainders_5(numbers_1)))
print(all(remainders_5(numbers_2)))
print(all(remainders_5(numbers_3)))
num4 = all(remainders_5(numbers_4))
print(f"num4 = {num4}")

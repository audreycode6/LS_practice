# You want to add the numbers from 1 to 5 to a list,
# but the code below is not producing the expected result.
# How can you fix it?


numbers = []

for i in range(1, 6):  # change start and stop of range
    # start at 1 and stop at 5
    # i.e 6 b/c it stops before reaching the stop limit
    numbers.append(i)

print(numbers)  # [1, 2, 3, 4, 5]

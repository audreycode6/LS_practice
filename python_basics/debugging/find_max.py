# Your colleague has implemented a custom function to find the maximum value
# in a list. However, the function sometimes works correctly, but other times
# it produces incorrect results. Can you help your colleague fix the bug?


def find_maximum(numbers):
    if not numbers:
        return None
    max_number = numbers[0]
    # OR initialize to numbers[0] so it checks first value in numbers to rest,
    # returning the lowest
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number


print(find_maximum([45, 3, 10, 98, 22]))  # Expected 98
print(find_maximum([-1, 0, 5, 3]))  # Expected 5
print(find_maximum([-10, -3, -20, -2]))  # Expected -2
print(find_maximum([]))  # Expected None


print()
# ERROR: currently if given negatives in arg, 0 is set at max_number
# and that might not be a number in arg


# FIX using max()
def find_max(nums):
    if not nums:
        return None
    else:
        return max(nums)


print(find_max([45, 3, 10, 98, 22]))  # Expected 3
print(find_max([-1, 0, 5, 3]))  # Expected 5
print(find_max([-10, -3, -20, -2]))  # Expected -2
print(find_max([]))  # Expected None

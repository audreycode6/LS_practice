# Write a function that compares the length of two strings.
# It should return -1 if the first string is shorter,
# 1 if the second string is shorter, and 0 if they're of equal length.
# For example:
# compare_by_length('patience', 'perseverance') # -1
# compare_by_length('strength', 'dignity')      #  1
# compare_by_length('humor', 'grace')           #  0

str1 = input("Enter a word: ")
str2 = input("Enter another word: ")


def compare_by_length(str1, str2):
    length1 = len(str1)
    length2 = len(str2)
    if length1 > length2:
        print(1)
    elif length1 < length2:
        print(-1)
    else:
        print(0)


compare_by_length(str1, str2)

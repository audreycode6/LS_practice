# Count the number of elements in scores that are 100 or above.

scores = [96, 47, 113, 89, 100, 102]
scores_100_plus = 0  # variable to track scores >= 100

for score in scores:  # loop through scores list to check each elements value
    if score >= 100:
        scores_100_plus += 1  # increase if condition is met
print(scores_100_plus)  # 3

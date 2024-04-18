# We wanted to create a matrix 3x3 so we could use it to build a Tic-Tac-Toe
# game. However, we encountered an issue, as whenever we change a value in
# one nested list, all nested lists are affected. Can you fix the code?
#
sub_list = ["-", "-", "-"]
matrix = []


# ERROR: when you alter a nested ALL list's in nested list are altered
# for _ in range(3):
# matrix.append(sub_list) # <-- ERROR: need to make a shallow copy
# matrix[0][0] = "X"
# print(matrix) # [['X', '-', '-'], ['X', '-', '-'], ['X', '-', '-']]

for _ in range(3):
    matrix.append(sub_list.copy())  # use .copy() to store shallow copy

# TEST:
matrix[0][0] = "X"  # alter
print(matrix)  # output: ['X', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
matrix[1][1] = "O"  # alter
print(matrix)  #  output: [['X', '-', '-'], ['-', 'O', '-'], ['-', '-', '-']]

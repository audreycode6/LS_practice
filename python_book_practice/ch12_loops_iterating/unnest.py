# Print all of the even numbers in the following list of nested lists.
# This time, don't use any for loops.

my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]

# Ls way
outer_index = 0
while outer_index < len(my_list):
    inner_list = my_list[outer_index]
    inner_index = 0
    while inner_index < len(inner_list):
        number = inner_list[inner_index]
        if number % 2 == 0:
            print(number)
        inner_index += 1
    outer_index += 1

print()
# OR my way

list_1 = my_list[0]
list_2 = my_list[1]
list_3 = my_list[2]

index1 = 0
while len(list_1) > index1:
    inner_list1 = list_1[index1]
    if inner_list1 % 2 == 0:
        print(inner_list1)
    index1 += 1

index2 = 0
while len(list_2) > index2:
    inner_list2 = list_2[index2]
    if inner_list2 % 2 == 0:
        print(inner_list2)
    index2 += 1

index3 = 0
while len(list_3) > index3:
    inner_list3 = list_3[index3]
    if inner_list3 % 2 == 0:
        print(inner_list3)
    index3 += 1

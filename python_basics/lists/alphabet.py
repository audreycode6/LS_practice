# Split the string alphabet into a list of characters.

alphabet = "abcdefghijklmnopqrstuvwxyz"
letter_list = []  # initialize empty list

for letter in alphabet:  # loop each char in alphabet
    letter_list.append(letter)  # add new list element for each letter to letter_list
print(letter_list)
# 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# OR use list() constructor

alphabet1 = "abcdefghijklmnopqrstuvwxyz"
new_alpha_list = list(alphabet1)

# TEST
print(new_alpha_list)
# 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

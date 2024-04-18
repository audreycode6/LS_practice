# Using the following code, compare the value of name with the string 'RoGeR'
# while ignoring the case of both strings. Print true if the values are
# the same; print false if they aren't.
# Next, perform a case-insensitive comparison between the value of name
# and the string 'DAVE'.

name = "Roger"
name2 = "RoGeR"

if name.capitalize() == name2.capitalize():
    print(True)
else:
    print(False)

# str.casefold is mopst accurate for comparing without caring about case of a str
string1 = input("Enter a word to compare: ")
string2 = input("Enter a word to compare: ")
if string1.casefold() == string2.casefold():
    print(True)
else:
    print(False)

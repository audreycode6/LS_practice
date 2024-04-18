# Use Python's string methods on the string 'Captain Ruby'
# to create a string with the value 'Captain Python'.

string1 = "Captain Ruby"

# str.replace() method
captain_python = string1.replace("Ruby", "Python")
print(captain_python)  # Captain Python

# OR str.removesuffix() method
new_string = string1.removesuffix("Ruby")  # Captain
python_captain = new_string + "Python"  # concatenate 'Captain' with 'Python'
print(python_captain)  # Captain Python

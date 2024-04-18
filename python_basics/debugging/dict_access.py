# You are trying to access a value in a dictionary,
# but the code is giving you an error.
# Can you change line 3 so that it prints "Unknown"
# instead of raising an error?


info = {"name": "Srdjan", "age": 38}

# print(info["city"])  # Error calling key that doesn't exist

print(info.get("city", "Unknown"))
# use dict.get() to find a key/value you aren't sure exists,
# takes optional arg for default return if not existing

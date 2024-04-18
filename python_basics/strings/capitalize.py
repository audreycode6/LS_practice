# Write code that capitalizes the words in the string
# 'launch school tech & talk', so that you get the string
# 'Launch School Tech & Talk'.

print("launch school tech & talk".title())


# OR if you dont use str.title():
def capitalize_words(string):
    words = string.split(" ")
    capitalized_words = []

    for word in words:
        cap_words = word.capitalize()
        capitalized_words.append(cap_words)
    return " ".join(capitalized_words)


string = "launch school tech & talk"
result = capitalize_words(string)
print(result)  # Launch School Tech & Talk

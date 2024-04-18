# You've been given a list of vocabulary words grouped into sub-lists,
# by meaning. This is a two-dimensional list or a nested list.

# Write some code that iterates through and prints all the words,
# one per line.

vocabulary = [
    ["happy", "cheerful", "merry", "glad"],
    ["tired", "sleepy", "fatigued", "drained"],
    ["excited", "eager", "enthused", "animated"],
]
# nested for loop
for list in vocabulary:  # loop through lists in vocabulary
    for word in list:  # loop through words in each list
        print(word)  # print each word

        # happy
        # cheerful
        # merry
        # glad
        # tired
        # sleepy
        # etc...

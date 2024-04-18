# make new tuple and reassign stuff to it;
# grab range 0:2 (first 2 eleements) +  goodbye, element 3 (last element in original tuple)
stuff = ("hello", "world", "bye", "now")
stuff = stuff[0:2] + ("goodbye", stuff[3])
# print(stuff)

# OR make new tuple an reassign 'silly' to new tuple
silly = ("hello", "world", "bye", "now")
silly = ("hello", "world", "goodbye", "now")
# print(silly)

# OR  convert to list then convert back to tuple
thing = ("hello", "world", "bye", "now")
thing = list(thing)
thing[2] = "goodbye"
thing = tuple(thing)
print(thing)

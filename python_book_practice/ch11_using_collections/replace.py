# Write Python code to replace all the :
# characters in the string below with +.

# original str
info = "xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh"
print(f"{info} <-- original")

# str.split (specficy splitting :)
split_info = info.split(":")

# .join(str) (concatenate strings with +)
print("+".join(split_info))

# str.replace(old, new)
info2 = "xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh"
print(info2.replace(":", "+"))
# print(replaced)

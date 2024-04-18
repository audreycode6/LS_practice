print("sub" in "substring")  # True
print("stg" in "substring")  # False

string1 = "mischievous"
print(string1.find("vous"[0:10]))  # 7
print(string1.find("vos"[0:10]))  # -1

string = "butterfly"
print(string.index("fly"[0:8]))  # 6
# print(string.index("fre"[0:8])) # valueError

string2 = "butterfly"
print(string2.count("chick"[0:8]))  # 0
print(string2.count("butt"[0:8]))  # 1

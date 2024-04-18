# You want to have a small script delivering motivational quotes,
# but with the following code you run into a very common error message:
# TypeError: can only concatenate str (not "NoneType") to str.
# What is the problem and how can you fix it?


def get_quote(person):
    if person == "Yoda":
        return "Do. Or do not. There is no try."  # added return
    if person == "Confucius":
        return "I hear and I forget. I see and I remember. I do and I understand."  # added return
    if person == "Einstein":
        return "Do not worry about your difficulties in Mathematics. I can assure you mine are still greater."  # added return


print("Confucius says:")
print('"' + get_quote("Confucius") + '"')
# error no return statement so None was being returned
# print(get_quote("Confucius"))  # print none

print() # space to see different outputs
# personally would print with f string so it is neater:
print(f"Confucius says: '{get_quote("Confucius")}'")

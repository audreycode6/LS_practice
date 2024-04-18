# Modify the following code so the loop continues iterating until
# the user inputs 'yes'.

while True:
    print("Should I stop looping?")
    answer = input("Enter 'yes' to stop: ")
    lower_answer = answer.lower()
    if lower_answer == "yes":
        break

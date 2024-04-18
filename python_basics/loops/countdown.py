# The following code prints the numbers from 1 to 10.
# Modify it so that it instead prints the numbers from 10 to 1 in
# descending order, followed by 'Launch!'.

for i in range(10, 0, -1):  # start @ 10, stop @ 1 and step back by 1 each time
    print(i)
print("Launch!")  # unindent so it prints after countdown

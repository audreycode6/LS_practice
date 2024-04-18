# Our predict_weather function should output a message indicating whether
# a sunny or cloudy day lies ahead.
# However, the output is the same every time the function is invoked.
# Why? Fix the code so that it behaves as expected.

import random


def predict_weather():
    sunshine = random.choice([True, False])  # (["True", "False"])
    print(sunshine)
    # ERROR: using True or False as strings,
    # so if sunshine is always true with initial solution

    if sunshine:  # if sunshine == Truthy
        print("Today's weather will be sunny!")
    else:
        print("Today's weather will be cloudy!")


# OR change if condition to check string == "True"

# def predict_weather():
#     sunshine = random.choice(["True", "False"])
#     print(sunshine)
#     if sunshine == "True":
#         print("Today's weather will be sunny!")
#     else:
#         print("Today's weather will be cloudy!")


predict_weather()

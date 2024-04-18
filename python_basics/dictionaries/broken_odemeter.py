# 1. Using the following code, delete the 'mileage' key and
# its associated value from car.

car = {
    "type": "sedan",
    "color": "blue",
    "mileage": 80_000,
    "year": 2003,
}

del car["mileage"]  # del deletes key/value pair

# TEST
print(car)  # {'type': 'sedan', 'color': 'blue', 'year': 2003}

# 2. select and print the value 'blue' from the car object:

#  dict.get method.: returns the value associated with a given key if the
# key exists. Otherwise, it produces a default return value
print(car.get("color"))  # blue

# 3. Calculate and print the number of key/value pairs in the dictionary:

print(len(car))  # 3

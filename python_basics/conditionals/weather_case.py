# Take your code from the previous Check the Weather exercise and
# rewrite it as a match-case statement.
# Feel free to add more cases besides 'sunny' and 'rainy'.

weathers = {"rainy", "snowy", "windy", "sunny"}

for weather in weathers:
    match weather:
        case "rainy":
            print(f"The weather is {weather}! Grab your umbrella.")
        case "sunny":
            print(f"The weather is {weather}! It's a beautiful day!")
        case _:
            print(f"The weather is {weather}! Let's stay inside.")

speed = 0
acceleration = 24
braking_force = 19
is_moving = braking_force < acceleration and (speed > 0 or acceleration > 0)
print(is_moving)

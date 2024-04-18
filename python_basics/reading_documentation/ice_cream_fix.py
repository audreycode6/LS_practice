iceCreamDensity = 10  # not proper variable naming format, using camelCase, we use snake_case: ice_cream_density
# also not spacing between objects/operators, makes it hard to read --> ice_cream_density = 10

while iceCreamDensity > 0:  # spacing again makes it hard to read
    print("Drip...")
    iceCreamDensity -= 1

print("The ice cream melted.")

# proper format:
ice_cream_density = 10
while ice_cream_density > 0:
    print("Drip...")
    ice_cream_density -= 1
print("The ice cream melted.")

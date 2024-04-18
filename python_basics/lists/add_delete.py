# We are given the following list of energy sources.
# Write some code to remove 'fossil' from the list,
# then add 'geothermal' to the end of the list.

energy = ["fossil", "solar", "wind", "tidal", "fusion"]

energy = energy[1 : len(energy)]  # slice to remove "fossil"
energy = energy + ["geothermal"]  # concatenate energy with other list
print(energy)  # ['solar', 'wind', 'tidal', 'fusion', 'geothermal']

# OR more efficient to use methods: .remove() & .append()

energy1 = ["fossil", "solar", "wind", "tidal", "fusion"]
energy1.remove("fossil")  # remove 'fossil'
energy1.append("geothermal")  # add "geothermal" to end of list
print(energy1)  # ['solar', 'wind', 'tidal', 'fusion', 'geothermal']

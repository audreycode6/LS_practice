# Initialize a variable weather with a string value being 'sunny', 'rainy',
# or whatever weather condition you choose.
# Then, write an if statement that prints:
# It's a beautiful day! if weather's value is 'sunny'
# Grab your umbrella. if weather's value is 'rainy'
# Let's stay inside. if weather's value is anything else
# Test your code with different values for weather.

weathers = {"sunny", "rainy", "cloudy", "snowy", "dreary", "stormy"}
for weather in weathers:
    if weather == "sunny":
        print(f"The weather is {weather}! It's a beautiful day!")
    elif weather == "rainy":
        print(f"The weather is {weather}! Grab your umbrella.")
    else:
        print(f"The weather is {weather}! Let's stay inside.")

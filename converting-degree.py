# Create a function to convert Celsius to Fahrenheit
# First thing to do is to ask user for temperature in Celsius
temp = float(input("Enter temperature in Celsius:"))

# Perform calculation and convert the temperature into Fahrenheit
fahrenheit = (temp * 9/5) +32 # general formular for converting

# Print the temperature in Fahrenheit
print(f"{temp} in Celsius is equal to {fahrenheit} in Fahrenheit")

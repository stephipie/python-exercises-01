# Create a funtion to show the price of an article including tax
# First ask the user for Input of net price
temp = float(input("Please enter the net price of your article: "))

# Calculation
price_with_tax = (temp * 1.19)
x = round(price_with_tax, 2)

# Print the Price including tax
print(f"{temp} plus 19 % Tax is {x} €")
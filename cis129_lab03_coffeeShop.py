# This is an interactive text based Coffee Shop simulator
# It calculates a receipt based on how many items the user wants to order

# Welcome statement
print("Welcome to the \'Coffee Shop\' program\n")

# Get input from the user
coffeeCount = int(input("How many cups of coffee would you like? "))
muffinCount = int(input("How many muffins would you like? "))
sconeCount = int(input("How many scones would you like? "))
cupcakeCount = int(input("How many cupcakes would you like? "))

# Prices in dollars
coffeePrice = 5
muffinPrice = 4
sconePrice = 3
cupcakePrice = 6

# Calculate subtotals
coffeeSubtotal = coffeeCount * coffeePrice
muffinSubtotal = muffinCount * muffinPrice
sconeSubtotal = sconeCount * sconePrice
cupcakeSubtotal = cupcakeCount * cupcakePrice

# Calculate tax (6%)
taxRate = 0.06
tax = (coffeeSubtotal + muffinSubtotal + sconeSubtotal + cupcakeSubtotal) * taxRate

# Calculate total price
totalPrice = coffeeSubtotal + muffinSubtotal + sconeSubtotal + cupcakeSubtotal + tax

# Print the receipt

print("\n***************************************")
print("My Coffee and Muffin Shop")
print("Number of coffees bought?")
print(str(coffeeCount))
print("Number of muffins bought?")
print(str(muffinCount))
print("Number of scones bought?")
print(str(sconeCount))
print("Number of cupcakes bought?")
print(str(cupcakeCount))
print("***************************************")
print("\n")
print("***************************************")
print("My Coffee and Muffin Shop Receipt")
print(str(coffeeCount) + " Coffee(s) at $" + str(coffeePrice) + " each: $" + format(coffeeSubtotal, ".2f"))
print(str(muffinCount) + " Muffin(s) at $" + str(muffinPrice) + " each: $" + format(muffinSubtotal, ".2f"))
print(str(sconeCount) + " Scone(s) at $" + str(sconePrice) + " each: $" + format(sconeSubtotal, ".2f"))
print(str(cupcakeCount) + " Cupcake(s) at $" + str(cupcakePrice) + " each: $" + format(cupcakeSubtotal, ".2f"))
print(str(taxRate * 100) + "% tax: $" + format(tax, ".2f"))
print("---------")
print("Total: $" + format(totalPrice, ".2f"))
print("***************************************")
print("---Thank you for using the program, goodbye!---\n")

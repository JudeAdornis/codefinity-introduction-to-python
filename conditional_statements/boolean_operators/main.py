# Define the quantity of the item and the low stock threshold
total_cost = 25.00
discountEligible = total_cost >= 20.00

# Check if the item quantity is below the low stock threshold
#low_stock = milk_quantity <= low_stock_threshold

# Print the result
print("Is the purchase eligible for a discount?", discountEligible)
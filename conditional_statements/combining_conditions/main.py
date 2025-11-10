# Define the perishable and stock status conditions
# is_perishable = True
# item_quantity = 110
# perishable_highStockRisk = 100

# Using the (and) operator to combine two conditions
# The first condition (`is_perishable`) checks if the item is perishable
# The second condition (`item_quantity >= perishable_highStockRisk`) checks if the item is high in stock 
# The `consider_discount` variable will become `True` only if both conditions are `True`
# consider_discount = is_perishable and (item_quantity >= perishable_highStockRisk)

# Print the result
# print("Is the item perishable and high in stock?", consider_discount)
# The item's discount and stock status have been defined

# Define the seasonal and holiday status conditions 
# seasonal_item = False
# holiday_item = True

# Combine the conditions to check if the item is seasonal or discounted
# (`temporary_stock`) will become `True` if either condition `seasonal_item` OR `holiday_item` is `True`
# temporary_stock = seasonal_item or holiday_item

# Print the result
# print("Is this a seasonal or holiday item?", temporary_stock) 
discounted = False
lowStock = True
movingProduct = (discounted) or (lowStock)
promotion = not(discounted) and not(lowStock)
print("Is the item eligible for promotion?", promotion)

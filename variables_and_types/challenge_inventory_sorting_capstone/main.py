# Lists of items and categories for slicing
items = "Bubblegum, Chocolate, Pasta"
categories = "Candy Aisle, Pasta Aisle"

# Slice the items string to extract
candy1 = items[ :9]
candy2 = items[11:20]
dry_goods = items[22:27]

# Slice the categories string to extract
category1 = categories[ :11]
category2 = categories[13:24]

# Create price variables
bubblegum_price = "$1.50"
chocolate_price = "$2.00"
pasta_price = "$5.40"

# Using print() to display item names, prices, and categories
print("we have"+ " " +candy1+ " " + "for" + " " +bubblegum_price+ " " + "in the" + " " + category1)
print("we have"+ " " +candy2+ " " + "for" + " " +chocolate_price+ " " + "in the" + " " + category1)
print("we have"+ " " +dry_goods+ " " + "for" + " " +pasta_price+ " " + "in the" + " " + category2)
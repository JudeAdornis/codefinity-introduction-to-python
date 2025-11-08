grocery_items = "milk cheese bread apples oranges chicken"
# slicing the string in the variable "grocery_items"
dairy1 = grocery_items[ :4]
dairy2 = grocery_items[5:11]
bakery1 = grocery_items[12:17]

# Concatenating the slices to form a meanigful sentence
print("we have dairy and bakery items:" " " + dairy1 + "," " " + dairy2 + "," " " + "and" + " " + bakery1 + " " + "in aisle 5")

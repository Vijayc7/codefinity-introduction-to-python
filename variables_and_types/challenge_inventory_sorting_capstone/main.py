# Lists of items and categories for slicing
items = "Bubblegum, Chocolate, Pasta"
categories = "Candy Aisle, Pasta Aisle"

# Slice Items
candy1 = items[0:9]
candy2 = items[11:20]
dry_goods = items[22:]

# Categories
category1 = categories[0:11]
category2 = categories[13:]

# Create Price variables
bubblegum_price = "$1.50"
chocolate_price = "$2.00"
pasta_price = "$5.40"

mesg1 = f"We have {candy1} for {bubblegum_price} in the {category1}"
mesg2 = f"We have {candy2} for {chocolate_price} in the {category1}"
mesg3 = f"We have {dry_goods} for {pasta_price} in the {category2}"
print(mesg1)
print(mesg2)
print(mesg3)
# List of products with their initial stock levels at the start of the week
products = [
    ["Apples", 150],  
    ["Bananas", 200],
    ["Oranges", 100],
    ["Mangoes", 120]
]

# List of products sold by the end of the week
units_sold = [["Apples", 30], ["Bananas", 45], ["Oranges", 20], ["Mangoes", 10]]

# New shipment received at the end of the week
shipment_received = [["Apples", 50], ["Bananas", 70], ["Oranges", 30], ["Mangoes", 40]]

for index in range(len(products)):
    prod_list = products[index]
    sold_list = units_sold[index]
    if prod_list[0] == sold_list[0]:
       prod_list[1] = prod_list[1] - sold_list[1]
       products[index] = prod_list

# print(products)

for index2 in range(len(products)):
    ship_rec = shipment_received[index2]
    updt_prod = products[index2]
    if updt_prod[0] == ship_rec[0]:
        updt_prod[1] += ship_rec[1]
        products[index2] = updt_prod

print("Final stock levels for all products: ", products)
        
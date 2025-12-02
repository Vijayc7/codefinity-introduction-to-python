grocery_inventory = {"Milk": ("Dairy", 3.50, 8),
                    "Eggs": ("Dairy",5.50,30),
                    "Bread":("Bakery",2.99, 15),
                    "Apples":("Produce",1.50,50)}

eggs_data = grocery_inventory.get("Eggs")
eggs_price = eggs_data[1]
if eggs_price > 5:
    grocery_inventory.update({"Eggs": ("Dairy", 4.50,30)})
    print("Eggs are too expensive, reducing the price by $1.")
else:
    print("The price of egg is reasonable")

grocery_inventory.update({"Tomatoes":("Produce",1.20,30)}) 
print(f"Inventory after adding Tomatoes: {grocery_inventory}")

milk_data = grocery_inventory.get("Milk")
milk_stock = milk_data[2]
if milk_stock < 10:
    grocery_inventory.update({"Milk":("Dairy",3.50,28)})
    print("Milk needs to be restocked. Increasing stock by 20 units.")
else:
    print("Milk has sufficient stock.")

apples_data = grocery_inventory.get("Apples")
apples_price = apples_data[1]
if apples_price > 2:
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price.")

print(f"Updated inventory:{grocery_inventory}")
    
    
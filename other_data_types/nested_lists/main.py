# Define Individual grocery item Lists
# bread = ["Bread", 4.80, 3, "Gluten Free"]
# milk = ["Milk", 5.99, 2, "2% Milk"]
# apple = ["Apple", 1.27, 12, "Fuji"]

# grocery_list = [bread, milk, apple]
# print("Grocery List:" , grocery_list)

# print("Item:", grocery_list[2][0])
# print("Price:", grocery_list[2][1])

# tomatoes = ["Tomatoes", 2.59, 4, "Texan"]
# potatoes = ["Potatoes", 1.75, 3, "Red"]
# onions = ["Onions", 2.69, 5, "Lonestar"]

vegetables = ["tomatoes", "potatoes", "onions"]
vegetables.remove("onions")
vegetables.append("carrots")
vegetables.append("cucumbers")
vegetables.sort()
print(f"Updated Vegetable Inventory: {vegetables}")
if "carrots" in vegetables:
    print("Carrots are already in the list.")
if "cucumbers" in vegetables:
    print("Cucumbers are already in the list.")


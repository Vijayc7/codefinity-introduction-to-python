# Initialize the inventory dictionary with stock details
inventory = {
    "Bread": [30, 50, 10, False],   # "Item": [current stock, minimum stock, restock quantity, on sale (True/False)]
    "Eggs": [120, 200, 40, False],
    "Milk": [60, 100, 20, False],
    "Apples": [15, 50, 15, False]
}

discount_threshold = 100

print("Processing started")
for item_name,list in inventory.items():
    print(f"Processing {item_name}")
    while list[0] < list[1]:
        list[0] = list[0] + list[2]
    if list[0] > discount_threshold and list[3] == False:
        list[3] = True

print("Processing completed")


# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")
apple_count = shelf.count("apples")
print(f"Number of Apples: {apple_count}")
banana_index = shelf.index("bananas")
print(f"First Banana Index: {banana_index}")

if apple_count < 5:
    print(f"Apples need to be restocked.")
else:
    print(f"Apples are sufficiently stocked.")

count_grapes = shelf.count("grapes")
if count_grapes == 1:
    print("Grapes need to be restocked.")
else:
    print("Greapes are sufficiently stocked.")

# oranges_exist = shelf.__contains__("oranges")
oranges_exist = ("oranges" in shelf)
if oranges_exist == True:
    orange_index = shelf.index("oranges")
    print(f"Oranges are at index: {orange_index}")
else:
    print("Oranges are out of stock.")
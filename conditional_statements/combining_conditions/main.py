# The item's discount and stock status have been defined
discounted = False
lowStock = True
item_price = 5.69
item_quantity = 50
movingProduct = (item_price >= 6.00) or (item_quantity <= 100)
promotion = (item_price >= 6.00) and not(item_quantity <= 100)
print(f"Is the item eligible for promotion? {promotion}")
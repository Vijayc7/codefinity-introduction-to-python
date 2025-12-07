prices = [29.99, 45.50, 12.75, 38.20]
discount = 0.00

index_length = prices.__len__()

for index in range(len(prices)):
    item = prices[index]
    if index == 0:
        discount_factor = 10.00 / 100.00
        updated_price = item * discount_factor
        prices[index] = item - updated_price
        print(f"Updated price for item {item}: ${prices[index]:.2f}")
    elif index == 1:
        discount_factor = 20.00 / 100
        updated_price = item * discount_factor
        prices[index] = item - updated_price
        print(f"Updated price for item {item}: ${prices[index]:.2f}")
    elif index == 2:
        discount_factor = 15.00 / 100
        updated_price = item * discount_factor
        prices[index] = item - updated_price
        print(f"Updated price for item {item}: ${prices[index]:.2f}")
    elif index == 3:
        discount_factor = 5.00 / 100
        updated_price = item * discount_factor
        prices[index] = item - updated_price
        print(f"Updated price for item {item}: ${prices[index]:.2f}")
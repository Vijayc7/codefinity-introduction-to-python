# List of product prices
product_prices = [1.50, 2.50, 3.00, 0.99, 2.30]

def apply_discount(prices):
    price_copy = prices.copy()
    for index in range(len(price_copy)):
        if price_copy[index] > 2.00:
            discounted_price = ( 10 * price_copy[index] ) / 100
            price_copy[index] -= discounted_price 
    return price_copy
# Call the function and store the updated prices
updated_prices = apply_discount(product_prices)

print("Updated product prices: $", updated_prices)
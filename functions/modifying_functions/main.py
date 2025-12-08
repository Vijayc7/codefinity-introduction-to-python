def apply_discount(price,discount=0.05):
    discounted_price = price * (1 - discount)
    return discounted_price

def apply_tax(price, tax=0.07):
    updated_price = price * (1 + tax)
    return updated_price

def calculate_total(price, discount=0.05, tax=0.07):
    updt_price = apply_tax(price,tax) 
    total_price = apply_discount(updt_price,discount)
    return total_price

tot_price_default = calculate_total(120)
print(f"Total cost with default discount and tax: ${tot_price_default}")

total_price_custom = calculate_total(100,discount=0.10, tax=0.08)
print(f"Total cost with custom discount and tax: ${total_price_custom}")
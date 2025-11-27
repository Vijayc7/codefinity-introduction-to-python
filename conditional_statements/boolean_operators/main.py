total_cost = 25.00
disc_threshold = 20.00
discountEligible = total_cost >= disc_threshold

message = f"Is the purchase eligible for a discount? {discountEligible}"

print(message)
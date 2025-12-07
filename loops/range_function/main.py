# List of products on promotion for each weekday
daily_promotions = ["Milk", "Eggs", "Bread", "Apples", "Oranges"]

# List of weekdays corresponding to the promotions
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

range_count = daily_promotions.__len__()

for count in range(range_count):
    promotion = daily_promotions[count]
    weekday = weekdays[count]
    print(f"{weekday}: Promotion on {promotion}")

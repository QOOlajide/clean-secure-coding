# So did you guys know that I'm a barber?!
# Here are some of the things I can do as well as my hypothetical charges

hairstyles = ["light caesar", "dark caesar", "afro", "line-up", "taper", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 35, 50, 35]
last_week = [2, 3, 5, 4, 4, 6, 2]

# Calculate average price
total_price = sum(prices)
average_price = total_price / len(prices)
print(f"Average price: ${average_price:.2f}")

# New prices with $6 discount
new_prices = [price - 6 for price in prices]
print("New prices after $6 discount:", new_prices)

# Calculate total revenue for last week
total_revenue = 0
for i in range(len(hairstyles)):
    total_revenue += prices[i] * last_week[i]
print(f"Total revenue last week: ${total_revenue}")

# Average daily revenue assuming 7 days a week
average_daily_revenue = total_revenue / 7
print(f"Average daily revenue: ${average_daily_revenue:.2f}")

# Hairstyles with new prices under $30
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print("Hairstyles under $30:", cuts_under_30)

# Learned list comprehension, highlighting the flexibility of Python

#!/usr/bin/python3
# data
products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]
prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]

# total price average for all products
average_price = sum(prices) / len(prices)

# new price list reduced  by $5
new_prices = [price - 5 for price in prices]

# total revenue generated from the products
total_revenue = sum([price * quantity for price, quantity in zip(prices, last_week)])

# Calculate the average daily revenue generated from the products
average_daily_revenue = total_revenue / sum(last_week)

# Identify products with prices less than $30 based on new prices
products_less_than_30 = [product for product, price in zip(products, new_prices) if price < 30]

# Display the results
print(f"Average Price: ${average_price:.2f}")
print("New Prices:", new_prices)
print(f"Total Revenue: ${total_revenue:.2f}")
print(f"Average Daily Revenue: ${average_daily_revenue:.2f}")
print("Products with prices less than $30:", products_less_than_30)

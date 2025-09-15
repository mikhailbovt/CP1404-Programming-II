TAX_RATE = 0.05
price = float(input("Enter the price of the item: "))
government_tax = input("Has GST? ").upper()
if government_tax == "YES":
    price = price + (price * TAX_RATE)
print(f"The price of the item is ${price:.2f}")
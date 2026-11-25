import json

with open("products.json", "r") as file:
    products = json.load(file)

for product in products:
    value = product["Quantity"] * product["price"]
    print(f'{product["Product"]}: {value}')

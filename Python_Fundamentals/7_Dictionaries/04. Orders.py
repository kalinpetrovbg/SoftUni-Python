command = input()

product_prices = {}
product_qty = {}

while command != "buy":
    product, price, quantity = command.split()
    price = float(price)
    quantity = int(quantity)

    if product not in product_prices:
        product_prices[product] = price
        product_qty[product] = quantity
    else:
        product_prices[product] = price
        product_qty[product] += quantity

    command = input()

for product, prices in product_prices.items():
    total = prices * product_qty.get(product)
    print(f"{product} -> {total:.2f}")

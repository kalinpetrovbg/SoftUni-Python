text = input().split()
products = {}

for i in range(0, len(text), 2):
    item = text[i]
    qty = text[i + 1]
    products[item] = qty

search = list(input().split())

for each in search:
    if each in products:
        print(f"We have {products[each]} of {each} left")
    else:
        print(f"Sorry, we don't have {each}")
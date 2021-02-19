price = 7.61
land = float(input())
cost = land * price
discount = cost * 0.18
cost_discount = cost - discount
print(f'The final price is: {cost_discount} lv.')
print(f'The discount is: {discount} lv.')
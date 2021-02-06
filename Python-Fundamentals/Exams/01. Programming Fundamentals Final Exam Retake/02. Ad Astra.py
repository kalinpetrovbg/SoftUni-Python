import re

dci = 2000
string = input()
pattern = r'(#|\|)([A-Z][a-z]+(\s?[A-Z][a-z]+)*)\1(\d{2}\/\d{2}\/\d{2})\1([0-9]{1,5})\1'

matches = re.findall(pattern, string)

items_found = len(matches)

total_food_calories = 0
for i in range(items_found):
    total_food_calories += int(matches[i][-1])

days = total_food_calories // dci
print(f'You have food to last you for: {days} days!')

for i in range(items_found):
    item_name = matches[i][1]
    expiration_date = matches[i][-2]
    calories = int(matches[i][-1])
    print(f'Item: {item_name}, Best before: {expiration_date}, Nutrition: {calories}')
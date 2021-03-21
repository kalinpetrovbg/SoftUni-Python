days = int(input())
budget = float(input())
people = int(input())
fuel_price = float(input())
food_person = float(input())
room_price = float(input())

daily_cost = 0
current_expenses = 0
day = 1
hotel = (food_person * people * days) + (room_price * people * days)

while current_expenses <= budget:

    distance = int(input())
    fuel = distance * fuel_price
    daily_cost = hotel + fuel
    current_expenses += daily_cost
    hotel = 0

    if day % 3 == 0 or day % 5 == 0 or day % 6 == 0:
        current_expenses *= 1.4

    if day % 7 == 0:
        current_expenses = current_expenses - (current_expenses / people)

    day += 1

    if day > days:
        break

budget -= current_expenses

if current_expenses < budget:
    print(f"You have reached the destination. You have {budget:.2f} budget left.")
else:
    print(f"Not enough money to continue the trip. You need {current_expenses:.2f}$ more.")




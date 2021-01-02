budget = float(input())
flour_price = float(input())

counter_cozonacs = 0
coloredEggs = 0
moneyLeft = 0

eggs_price = flour_price * 0.75
milk_price = (flour_price * 1.25) / 4
cozonac = eggs_price + flour_price + milk_price
rem_coloredEggs = 0

while budget >= cozonac:
    budget -= cozonac
    counter_cozonacs += 1
    coloredEggs += 3
    if counter_cozonacs % 3 == 0:
        rem_coloredEggs = counter_cozonacs - 2
    coloredEggs -= rem_coloredEggs
    rem_coloredEggs = 0

print(f"You made {counter_cozonacs} cozonacs! Now you have {coloredEggs} eggs and {budget:.2f}BGN left.")
import math
party_size = int(input())
days = int(input())
sum_coins = 0
avrg_coins = 0

for x in range(1, days + 1):
    if x % 10 == 0:
        party_size -= 2
    if x % 15 == 0:
        party_size += 5
    coins = 50 - (2 * party_size)
    sum_coins += coins
    if x % 3 == 0:
        sum_coins -= 3 * party_size
    if x % 5 == 0:
        sum_coins += 20 * party_size
        if x % 3 == 0:
            sum_coins -= 2 * party_size
avrg_coins = sum_coins / party_size
print(f"{party_size} companions received {math.floor(avrg_coins)} coins each.")
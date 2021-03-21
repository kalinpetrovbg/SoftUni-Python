capacity = 255
num = int(input())
water = 0
liters = 0
remaining_capacity = 0

for x in range(num):
    liters = int(input())
    water += liters
    if water > capacity:
        print("Insufficient capacity!")
        water -= liters
print(water)
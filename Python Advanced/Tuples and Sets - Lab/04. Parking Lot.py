num_cars = int(input())
parking = set()

for x in range(num_cars):
    what, plate = input().split(", ")
    if what == "IN":
        parking.add(plate)
    else:
        parking.remove(plate)

if parking:
    for each in parking:
        print(each)
else:
    print("Parking Lot is Empty")
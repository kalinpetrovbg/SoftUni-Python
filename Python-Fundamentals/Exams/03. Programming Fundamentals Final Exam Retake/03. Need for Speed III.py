n = int(input())
cars = {}

for _ in range(n):
    car, mileage, fuel = input().split("|")
    cars[car] = [int(mileage), int(fuel)]

commands = input()

while commands != "Stop":
    data = commands.split(" : ")

    if data[0] == "Drive":
        car, distance, petrol = data[1:]
        distance = int(distance)
        petrol = int(petrol)
        if petrol <= cars[car][1]:
            cars[car][0] += distance
            cars[car][1] -= petrol
            print(f"{car} driven for {distance} kilometers. {petrol} liters of fuel consumed.")
            if cars[car][0] >= 100000:
                print(f"Time to sell the {car}!")
                del cars[car]
        else:
            print(f"Not enough fuel to make that ride")

    elif data[0] == "Refuel":
        car, petrol = data[1:]
        petrol = int(petrol)
        if petrol + cars[car][1] > 75:
            petrol = 75 - cars[car][1]
        cars[car][1] += petrol
        print(f"{car} refueled with {petrol} liters")

    elif data[0] == "Revert":
        car, km = data[1:]
        km = int(km)
        cars[car][0] -= km
        if cars[car][0] < 10000:
            cars[car][0] = 10000
        else:
            print(f"{car} mileage decreased by {km} kilometers")

    commands = input()

for car, mils in sorted(cars.items(), key=lambda x: (-x[1][0], x[0])):
    print(f"{car} -> Mileage: {cars[car][0]} kms, Fuel in the tank: {cars[car][1]} lt.")

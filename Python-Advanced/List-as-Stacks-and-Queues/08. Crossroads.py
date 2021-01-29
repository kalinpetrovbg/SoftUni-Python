from collections import deque

green_light_duration = int(input())
can_pass = int(input())
command = input()

cars = deque()
counter = 0
crash = False

while command != "END":

    if command != "green":
        car = command
        cars.append(car)

    else:
        if cars:
            current_car = cars.popleft()
            current_car_length = len(current_car)
            free_to_pass = green_light_duration - current_car_length

            while free_to_pass > 0:
                counter += 1
                if len(cars) > 0:
                    current_car = cars.popleft()
                    free_to_pass -= len(current_car)
                else:
                    break

            if free_to_pass == 0:
                counter += 1
            if can_pass >= abs(free_to_pass):
                if free_to_pass < 0:
                    counter += 1
            else:
                none = can_pass + free_to_pass
                print("A crash happened!")
                print(f"{current_car} was hit at {current_car[none]}.")
                crash = True
                break

    command = input()

if not crash:
    print("Everyone is safe.")
    print(f"{counter} total cars passed the crossroads.")




    command = input()

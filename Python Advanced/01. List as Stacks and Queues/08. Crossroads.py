from collections import deque

green = int(input())
window = int(input())
command = input()
cars = deque()
passed = 0
crash = False

while command != "END":
    if crash:
        break

    if command != "green":
        cars.append(command)

    elif command == "green":
        time = green
        extra_time = window

        while time > 0:
            if cars:
                current_car = cars.popleft()
                auto = current_car
            else:
                break

            for i in range(len(current_car)):
                current_car = list(current_car)
                char = current_car.pop(0)
                if len(current_car) == 0:
                    passed += 1
                time -= 1
                if time < 0:
                    extra_time -= 1
                    if extra_time < 0:
                        print("A crash happened!")
                        print(f"{auto} was hit at {char}.")
                        crash = True
                        break
    command = input()

if not crash:
    print(f"Everyone is safe.")
    print(f"{passed} total cars passed the crossroads.")
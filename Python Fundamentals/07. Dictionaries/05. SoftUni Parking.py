n = int(input())
parking = {}

for _ in range(n):
    commands = input().split()

    if len(commands) == 3:
        _, name, plate = commands
        if name not in parking:
            print(f"{name} registered {plate} successfully")
            parking[name] = plate
        else:
            print(f"ERROR: already registered with plate number {plate}")

    elif len(commands) == 2:
        _, name = commands
        if name not in parking:
            print(f"ERROR: user {name} not found")
        else:
            print(f"{name} unregistered successfully")
            del parking[name]

for name, plate in parking.items():
    print(f"{name} => {plate}")

trip = input()
data = input()

while data != "Travel":
    text = data.split(":")
    command = text[0]

    if command == "Add Stop":
        index = int(text[1])
        new_str = text[2]
        if index in range(len(trip)):
            trip = trip[:index] + new_str + trip[index:]

    elif command == "Remove Stop":
        start = int(text[1])
        end = int(text[2])
        if start in range(len(trip)) and end in range(len(trip)):
            trip = trip[:start] + trip[end + 1:]

    elif command == "Switch":
        old = text[1]
        new = text[2]
        if old in trip:
            trip = trip.replace(old, new)

    print(trip)
    data = input()

print(f"Ready for world tour! Planned stops: {trip}")

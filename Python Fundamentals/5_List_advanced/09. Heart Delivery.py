houses = input().split("@")
command = input()
position = 0
failed = 0
house = [int(el) for el in houses]

while command != "Love!":

    jump, length = command.split()
    length = int(length)
    position += length

    if True:     # correct position
        if position >= len(house):
            position = 0
        house[position] -= 2

    if True:
        if house[position] == 0:
            print(f"Place {position} has Valentine's day.")

        elif house[position] < 0:
            print(f"Place {position} already had Valentine's day.")

    command = input()

for index in range(len(house)):
    if house[index] > 0:
        failed += 1

print(f"Cupid's last position was {position}.")

if failed == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {failed} places.")

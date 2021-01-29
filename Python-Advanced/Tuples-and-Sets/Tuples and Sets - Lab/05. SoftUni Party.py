num = int(input())
invited = set()

for _ in range(num):
    invited.add(input())

command = input()
while command != "END":
    person = command

    if person in invited:
        invited.remove(person)
    command = input()
print(len(invited))
print("\n".join(sorted(invited)))
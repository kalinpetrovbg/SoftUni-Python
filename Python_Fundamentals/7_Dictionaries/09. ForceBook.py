text = input()
users = {}
result = {}

while text != "Lumpawaroo":

    if "|" in text:
        side, user = text.split(" | ")
        if user not in users:
            users[user] = side

    if "->" in text:
        user, side = text.split(" -> ")
        users[user] = side
        print(f"{user} joins the {side} side!")

    text = input()

for user, side in users.items():
    if side not in result:
        result[side] = []
        result[side].append(user)
    else:
        result[side].append(user)

result = dict(sorted(result.items(), key=lambda x: (-len(x[1]), x[0])))
for key, value in result.items():
    print(f"Side: {key}, Members: {len(value)}")
    [print(f"! {name}") for name in sorted(value)]
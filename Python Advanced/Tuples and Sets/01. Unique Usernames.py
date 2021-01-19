num = int(input())
usernames = set()

for _ in range(num):
    usernames.add(input())

print("\n".join(usernames))
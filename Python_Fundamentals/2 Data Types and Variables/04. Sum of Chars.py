num = int(input())
sume = 0

for x in range(num):
    letter = input()
    new = ord(letter)
    sume += new
print(f"The sum equals: {sume}")
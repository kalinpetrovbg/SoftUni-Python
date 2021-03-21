n = int(input())

for _ in range(n):
    text = input()

    name = text[text.find("@") + 1: text.find("|")]
    age = text[text.find("#") + 1: text.find("*")]

    print(f"{name} is {age} years old.")
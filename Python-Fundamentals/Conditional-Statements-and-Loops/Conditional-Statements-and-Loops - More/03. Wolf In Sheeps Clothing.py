text = input().split(", ")
eaten = ""

if text[-1] == "wolf":
    print("Please go away and stop eating my sheep")

else:
    for index in range(len(text)):
        if text[index] == "wolf":
            eaten = len(text) - (index + 1)
    print(f"Oi! Sheep number {eaten}! You are about to be eaten by a wolf!")
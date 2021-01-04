cards = input().split()
num = int(input())
half = len(cards) // 2
result = []

for _ in range(num):
    result = []
    for index in range(len(cards)):
        if index == len(cards) / 2:
            break
        left_cards = cards[index]
        right_cards = cards[half + index]
        result.append(left_cards)
        result.append(right_cards)
    cards = result
print(result)
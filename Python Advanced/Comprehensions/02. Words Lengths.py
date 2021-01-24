strings = input().split(", ")

print(*[f"{word} -> {len(word)}" for word in strings], sep=", ")
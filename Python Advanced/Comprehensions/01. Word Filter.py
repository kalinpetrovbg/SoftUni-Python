text = input().split()

print(* [word for word in text if len(word) % 2 == 0], sep="\n")
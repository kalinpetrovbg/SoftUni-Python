c = input()
coffee = 0

while c != "END":

    if c == "coding" or c == "dog" or c == "cat" or c == "movie":
        coffee += 1
    elif c == "CODING" or c == "DOG" or c == "CAT" or c == "MOVIE":
        coffee += 2
    c = input()

if coffee > 5:
    print("You need extra sleep")
else:
    print(coffee)

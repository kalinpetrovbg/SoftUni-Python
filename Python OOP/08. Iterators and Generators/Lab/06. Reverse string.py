def reverse_text(string):
    for x in range(len(string) - 1, -1, -1):
        yield string[x]


for char in reverse_text("step"):
    print(char, end='')

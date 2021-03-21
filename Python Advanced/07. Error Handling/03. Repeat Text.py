text = input()
repeat = input()

try:
    print(text * int(repeat))
except ValueError:
    print("Variable times must be an integer")

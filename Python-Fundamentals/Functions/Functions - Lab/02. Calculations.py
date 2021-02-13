method = input()
num_1 = int(input())
num_2 = int(input())


def calculator(a, b, text):
    if text == "add":
        return a + b
    elif text == "subtract":
        return a - b
    elif text == "multiply":
        return a * b
    elif text == "divide":
        return a // b


print(calculator(num_1, num_2, method))
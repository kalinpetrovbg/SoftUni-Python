number1, number2 = input().split(" ")
number1 = int(number1)
number2 = int(number2)
num1 = set()
num2 = set()

for _ in range(number1):
    num1.add(input())

for _ in range(number2):
    num2.add(input())

result = num1 & num2
print("\n".join(result))
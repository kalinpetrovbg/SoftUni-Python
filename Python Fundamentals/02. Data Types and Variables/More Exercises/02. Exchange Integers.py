num1 = input()
a = num1
num2 = input()
b = num2
num1, num2 = num2, num1

print("Before:")
print(f"a = {a}")
print(f"b = {b}")
print("After:")
print(f"a = {num1}")
print(f"b = {num2}")
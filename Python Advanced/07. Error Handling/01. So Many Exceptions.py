numbers_list = input().split(", ")
result = 1

for i in range(len(numbers_list)):
    number = int(numbers_list[i])
    if number <= 5:
        result *= number
    elif 5 < number <= 10:
        result /= number

print(int(result))

# 1, 4, 5  = 20
# 4, 5, 6, 1, 3  = 10
# 2, 5, 10  = 1

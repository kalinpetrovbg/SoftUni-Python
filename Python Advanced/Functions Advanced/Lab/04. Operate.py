def operate(operator, *args):
    result = 0
    if operator == "+":
        for num in args:
            result += num
    elif operator == "-":
        for index in range(len(args)):
            if index == 0:
                result = args[0]
            else:
                result -= args[index]
    elif operator == "*":
        result = 1
        for num in args:
            result *= num
    else:
        for index in range(len(args)):
            if index == 0:
                result = args[0]
            else:
                result /= args[index]
    return result

# print(operate("+", 1, 2, 3))
# print(operate("*", 3, 4))


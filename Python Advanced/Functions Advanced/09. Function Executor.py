def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2

def func_executor(*args):
    output = []
    for functions, numbers in args:
        result = functions(*numbers)
        output.append(result)
    return output

print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
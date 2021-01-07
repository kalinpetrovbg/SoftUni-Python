def exchange(arr, index):
	if index <= -1 or index >= len(arr):
		print("Invalid index")
		return arr
	arr = arr[index + 1:] + arr[:index + 1]
	return arr


def max_even(arr):
	found = False
	index = None
	max_even_num = 0
	for i in range(len(arr)):
		if arr[i] % 2 == 0:
			found = True
			if arr[i] >= max_even_num:
				max_even_num = arr[i]
				index = i
	if not found:
		return "No matches"
	else:
		return index


def max_odd(arr):
	found = False
	index = None
	max_odd_num = 0
	for i in range(len(arr)):
		if arr[i] % 2 != 0:
			found = True
			if arr[i] >= max_odd_num:
				max_odd_num = arr[i]
				index = i
	if not found:
		return "No matches"
	else:
		return index


def min_even(arr):
	found = False
	index = None
	min_even_num = 1001
	for i in range(len(arr)):
		if arr[i] % 2 == 0:
			found = True
			if arr[i] <= min_even_num:
				min_even_num = arr[i]
				index = i
	if not found:
		return "No matches"
	else:
		return index


def min_odd(arr):
	found = False
	index = None
	min_odd_num = 1001
	for i in range(len(arr)):
		if arr[i] % 2 != 0:
			found = True
			if arr[i] <= min_odd_num:
				min_odd_num = arr[i]
				index = i
	if not found:
		return "No matches"
	else:
		return index


def first_even(arr, count):
	result = []
	if count > len(arr) or count <= 0:
		return "Invalid count"
	for num in arr:
		if num % 2 == 0 and count > 0:
			result.append(num)
			count -= 1
	return result


def first_odd(arr, count):
	result = []
	if count > len(arr) or count <= 0:
		return "Invalid count"
	for num in arr:
		if num % 2 != 0 and count > 0:
			result.append(num)
			count -= 1
	return result


def last_even(arr, count):
	result = []
	if count > len(arr) or count <= 0:
		return "Invalid count"
	for index in range(len(arr) - 1, -1, -1):
		if arr[index] % 2 == 0 and count > 0:
			result.append(arr[index])
			count -= 1
	result = result[::-1]
	return result


def last_odd(arr, count):
	result = []
	if count > len(arr) or count <= 0:
		return "Invalid count"
	for index in range(len(arr) - 1, -1, -1):
		if arr[index] % 2 != 0 and count > 0:
			result.append(arr[index])
			count -= 1
	result = result[::-1]
	return result


def array_manipulator():
	array_string = input()
	array = [int(n) for n in array_string.split()]

	while True:
		command = input().split()
		if command[0] == "end":
			print(array)
			break
		elif command[0] == "exchange":
			array = exchange(array, int(command[1]))
		elif command[0] == "max":
			if command[1] == "even":
				print(max_even(array))
			elif command[1] == "odd":
				print(max_odd(array))
		elif command[0] == "min":
			if command[1] == "even":
				print(min_even(array))
			elif command[1] == "odd":
				print(min_odd(array))
		elif command[0] == "first":
			if command[2] == "even":
				print(first_even(array, int(command[1])))
			elif command[2] == "odd":
				print(first_odd(array, int(command[1])))
		elif command[0] == "last":
			if command[2] == "even":
				print(last_even(array, int(command[1])))
			elif command[2] == "odd":
				print(last_odd(array, int(command[1])))


array_manipulator()

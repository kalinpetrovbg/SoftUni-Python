numbers = [int(el) for el in input().split()]
data = input()
good_list = []

while not data == "end":

    if "reverse" in data:
        my_nums = data.split()
        start = my_nums[2]
        start = int(start)
        count = my_nums[4]
        count = int(count)
        range = abs(start) + count

        if start > 0:
            list1 = numbers[0:start]
            list2 = numbers[start:range]
            list3 = numbers[range:]
            list2.reverse()

        elif start == 0:
            list1 = numbers[0:start]
            list2 = numbers[start:range]
            list3 = numbers[range:]

        elif start <= 0:
            list1 = numbers[0:range - 1]
            list2 = numbers[range - 1:start + 1]
            list3 = numbers[start + 1:]
            list2.reverse()

        good_list = list1 + list2 + list3
        good_list_str = [str(el) for el in good_list]
        print(", ".join(good_list_str))
        numbers = good_list

    elif "sort" in data:
        my_nums = data.split()
        start = my_nums[2]
        start = int(start)
        count = my_nums[4]
        count = int(count)
        range = abs(start) + count

        if start > 0:
            list1 = numbers[0:start]
            list2 = numbers[start:range]
            list3 = numbers[range:]
            list2.sort()

        elif start < 0:
            list1 = numbers[0:range - 1]
            list2 = numbers[range - 1:start + 1]
            list3 = numbers[start + 1:]
            list2.sort()

        good_list = list1 + list2 + list3
        good_list_str = [str(el) for el in good_list]
        print(", ".join(good_list_str))
        numbers = good_list

    elif "remove" in data:
        my_nums = data.split()
        num_int = my_nums[1]
        num_int = int(num_int)
        del numbers[0:num_int]
        good_list_str = [str(el) for el in numbers]
        print(", ".join(good_list_str))
        numbers = good_list

    data = input()

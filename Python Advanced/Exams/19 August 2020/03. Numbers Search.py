import collections

def numbers_searching(*args):
    result = []
    list1 = sorted(list(dict.fromkeys(args)))
    list1 = [x for x in range(list1[0], list1[-1]+1) if x not in list1]
    list2 = sorted([item for item, count in collections.Counter(args).items() if count > 1])

    result.append(*list1)
    result.append(list2)
    return result

print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
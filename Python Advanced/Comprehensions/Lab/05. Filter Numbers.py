start = int(input())
end = int(input())

def good_num(x):
    return any(x % i == 0 for i in range(2, 11))

print([x for x in range(start, end + 1) if good_num(x)])

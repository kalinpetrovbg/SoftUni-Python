def best_list_pureness(*test):
    k = test[1]
    rotator = test[0]
    max_result = -999999
    turns = 0

    for i in range(k + 1):
        current = list(enumerate(rotator))
        total = sum([(a * b) for a, b in current])
        num = rotator.pop()
        rotator.insert(0, num)

        if total > max_result:
            max_result = total
            turns = i

    return f"Best pureness {max_result} after {turns} rotations"

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)



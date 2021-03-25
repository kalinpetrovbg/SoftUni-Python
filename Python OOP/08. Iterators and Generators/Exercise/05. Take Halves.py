def solution():
    def integers():
        for x in range(1, 9999):
            yield x

    def halves():
        for x in integers():
            yield x / 2

    def take(n, seq):
        nums = []
        for x in seq:
            if len(nums) == n:
                return nums
            nums.append(x)

    return take, halves, integers

take = solution()[0]
halves = solution()[1]
print(take(5, halves()))



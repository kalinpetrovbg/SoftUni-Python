def make_expressions(list_nums, expression='', total=0):
    if not list_nums:
        return [(expression, total)]
    plus = make_expressions(
        list_nums[1:], expression=f'{expression}+{list_nums[0]}', total=total + list_nums[0])
    minus = make_expressions(
        list_nums[1:], expression=f'{expression}-{list_nums[0]}', total=total - list_nums[0])

    return plus + minus

numbers = [int(x) for x in input().split(", ")]
[print(f'{exp}={res}') for exp, res in make_expressions(numbers)]
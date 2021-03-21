def odd_vs_even():
    even = 0
    odd = 0
    numbers = input()
    for number in numbers:
        if int(number) % 2 == 0:
            even += int(number)
        else:
            odd += int(number)

    print(f"Odd sum = {odd}, Even sum = {even}")


odd_vs_even()

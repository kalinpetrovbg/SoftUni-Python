def perfect_num(parameter):
    sum_divisors = 0
    for i in range(1, parameter):
        if parameter % i == 0:
            sum_divisors += i
    if sum_divisors == parameter:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


number = int(input())

perfect_num(number)
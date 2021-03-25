def get_primes(ll):
    for each in ll:
        if each < 2:
            continue
        is_prime = True
        for i in range(2, each):
            if each % i == 0:
                is_prime = False
                break
        if is_prime:
            yield each

print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))
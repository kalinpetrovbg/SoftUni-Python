num = int(input())
prime = False

if num % 2 == 0 or num % 3 == 0:
    pass
else:
    prime = True

if not prime:
    print("False")
else:
    print("True")
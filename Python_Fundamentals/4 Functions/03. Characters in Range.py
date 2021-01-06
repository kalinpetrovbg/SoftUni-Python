def ancii_table(a, b):
    start = ord(a)
    end = ord(b)
    for each in range(start + 1, end):
        print(chr(each), end=" ")


ancii_table(input(), input())

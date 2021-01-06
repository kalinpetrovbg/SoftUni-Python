def palindrome():
    number = input().split(", ")
    for each in number:
        if each[::] == each[::-1]:
            print("True")
        else:
            print("False")


palindrome()
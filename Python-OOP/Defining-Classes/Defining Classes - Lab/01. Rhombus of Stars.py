def create_top_part(n):
    for i in range(n):
        print(" " * (n - i) + "* " * (i + 1))

def create_bottom_part(n):
    for j in range(n):
        print(" " * (j + 2) + "* " * (n - 1 - j))

num = int(input())

create_top_part(num)
create_bottom_part(num)
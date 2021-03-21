import math
from math import sqrt

def point1(coo1, coo2):
    return sqrt((coo1 ** 2) + (coo2 ** 2))

def point2(coo1, coo2):
    return sqrt((coo1 ** 2) + (coo2 ** 2))

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

res1 = math.floor(point1(x1, y1))
res2 = math.floor(point1(x2, y2))
if res1 <= res2:
    print(f"({int(x1)}, {int(y1)})")
else:
    print(f"({int(x2)}, {int(y2)})")
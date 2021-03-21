import math

n = int(input())
year = n * 100
days = year * 365.2422
days = math.floor(days)
hours = days * 24
mi = hours * 60

print(f"{n} centuries = {year} years = {days} days = {hours} hours = {mi} minutes")

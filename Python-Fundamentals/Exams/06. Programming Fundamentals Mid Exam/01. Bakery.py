import math

biscuits = int(input())
workers = int(input())
competitor = int(input())
total_per_month = 0
total_per_day = 0

for day in range(1, 31):
    total_per_day = biscuits * workers
    total_per_month += total_per_day

bad_day = total_per_day * 0.75
bad_day = math.floor(bad_day)

all_total = total_per_month - (10 * total_per_day)
all_total = all_total + (10 * bad_day)

print(f"You have produced {math.floor(all_total)} biscuits for the past month.")

percentage = (all_total - competitor) / competitor * 100
percentage2 = (competitor - all_total) / competitor * 100

if all_total > competitor:
    print(f"You produce {percentage:.2f} percent more biscuits.")
elif competitor > all_total:
    print(f"You produce {percentage2:.2f} percent less biscuits.")
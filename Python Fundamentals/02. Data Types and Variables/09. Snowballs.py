number = int(input())
biggest_snow = 0
snowball_snow = 0
snowball_time = 0
biggest_value = 0
snowball_quality = 0
biggest_time = 0
biggest_quality = 0

for x in range(1, number + 1):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    snowball_value = (snowball_snow / snowball_time) ** snowball_quality
    if snowball_value > biggest_value:
        biggest_value = snowball_value
        biggest_snow = snowball_snow
        biggest_time = snowball_time
        biggest_quality = snowball_quality
print(f"{biggest_snow} : {biggest_time} = {int(biggest_value)} ({biggest_quality})")
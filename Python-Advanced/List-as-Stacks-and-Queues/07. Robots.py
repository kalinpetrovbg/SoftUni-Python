from collections import deque
from datetime import datetime, timedelta

text = input().split(";")
time = datetime.strptime(input(), "%H:%M:%S")
time = time + timedelta(seconds=1)  # start the job 1 sec after given time

robots = []
av_robots = deque([])
products = []

for each in text:      # creating robots characteristics
    el = each.split("-")
    robot = {}
    robot['name'] = el[0]
    robot['time'] = int(el[1])
    robot['at'] = time
    robots.append(robot)
    av_robots.append(robot)    # creating queue with all available robots
av_robots = deque(av_robots)

product = input()

while product != "End":        # creating queue with all products
    products.append(product)
    product = input()
products = deque(products)

while len(products) > 0:
    current_product = products.popleft()

    if av_robots:
        current_robot = av_robots.popleft()
        current_robot['at'] = time + timedelta(seconds=current_robot['time'])
        robot = [el for el in robots if el == current_robot][0]
        robot['at'] = time + timedelta(seconds=current_robot['time'])
        print(f"{current_robot['name']} - {current_product} [{time.strftime('%H:%M:%S')}]")
    else:
        for r in robots:
            if time >= r['at']:
                av_robots.append(r)
        if not av_robots:
            products.append(current_product)
        else:
            current_robot = av_robots.popleft()
            current_robot['at'] = time + timedelta(seconds=current_robot['time'])
            robot = [el for el in robots if el == current_robot][0]
            robot['at'] = time + timedelta(seconds=current_robot['time'])
            print(f"{current_robot['name']} - {current_product} [{time.strftime('%H:%M:%S')}]")

    time = time + timedelta(seconds=1)



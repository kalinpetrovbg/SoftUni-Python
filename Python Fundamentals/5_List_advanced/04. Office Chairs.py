rooms = int(input())
free_chairs = 0

for room in range(rooms):
    chairs, people = input().split()
    av_chairs = int(len(chairs))
    people = int(people)
    room = room + 1
    if av_chairs >= people:
        free = av_chairs - people
        free_chairs += free
    else:
        free = people - av_chairs
        free_chairs -= free
        print(f"{people - av_chairs} more chairs needed in room {room}")

if free_chairs >= 0:
    print(f"Game On, {free_chairs} free chairs left")

command = input()
task_list = [0] * 10

while not command == "End":
    if command == "End":
        break
    data = command.split("-")
    index = int(data[0])
    task = data[1]
    task_list.insert(index, task)
    task_list.pop(index - 1)

    command = input()
    if "End" in command:
        break

counter = task_list.count(0)

for _ in range(counter):
    task_list.remove(0)

print(task_list)

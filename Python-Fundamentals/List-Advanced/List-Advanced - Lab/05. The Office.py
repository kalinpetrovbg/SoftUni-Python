employees_level = input().split()
improvement_factor = int(input())
all_employees = len(employees_level)
half_of_employees = len(employees_level) // 2
improved_list = []
total_anny = 0
level_to_int = [int(each) for each in employees_level]

for anny in level_to_int:
    result = anny * improvement_factor
    improved_list.append(result)
    total_anny += anny * improvement_factor

average_anny = total_anny / len(employees_level)
result = [every for every in improved_list if every >= average_anny]
in_good_mode = len(result)

if in_good_mode >= half_of_employees:
    print(f"Score: {in_good_mode}/{all_employees}. Employees are happy!")
else:
    print(f"Score: {in_good_mode}/{all_employees}. Employees are not happy!")

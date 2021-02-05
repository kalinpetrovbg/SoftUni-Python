nums = input().split()
command = input()
moves = 1
middle = 0

while not command == "end":

    middle = len(nums) // 2
    maxx = len(nums)
    num1, num2 = [int(el) for el in command.split()]

    if True:

        if num1 < 0 or num2 < 0 or num1 >= maxx or num2 >= maxx:     # wrong indexes
            print("Invalid input! Adding additional elements to the board")
            nums.insert(middle, f"-{moves}a")
            nums.insert(middle, f"-{moves}a")

        elif nums[num1] == nums[num2]:
            print(f"Congrats! You have found matching elements - {nums[num1]}!")
            if num1 > num2:
                nums.pop(num1)
                nums.pop(num2)
            else:
                nums.pop(num2)
                nums.pop(num1)

        elif num1 == num2:                                         # cheat - two equal indexes
            print("Invalid input! Adding additional elements to the board")
            nums.insert(middle, f"-{moves}a")
            nums.insert(middle, f"-{moves}a")

        elif nums[num1] != nums[num2]:
            print("Try again!")

    if len(nums) == 0:
        break

    command = input()
    moves += 1

if len(nums) > 0:
    print("Sorry you lose :(")
else:
    print(f"You have won in {moves} turns!")

print(*nums, end="")
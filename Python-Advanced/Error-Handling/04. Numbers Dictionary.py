numbers_dictionary = {}
line = input()

while line != "Search":
    number_as_string = line
    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print("The variable number must be an integer")
    line = input()

while line != "Remove":
    try:
        searched = input()
        print(numbers_dictionary[searched])
    except KeyError:
        print("{}")
    line = input()


while line != "End":
    searched = input()
    try:
        del numbers_dictionary[searched]
    except KeyError:
        print("Number does not exist in dictionary")
    line = input()

print(numbers_dictionary)

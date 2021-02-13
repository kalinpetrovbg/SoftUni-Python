num = int(input())
lines = int(input())
new_letter = ""
final = ""


for line in range(lines):
    letter = input()
    letter = ord(letter) + num
    new_letter = chr(letter)
    final += new_letter

print(final)
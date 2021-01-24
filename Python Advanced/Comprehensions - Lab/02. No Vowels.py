vowels = ['a', 'o', 'u', 'e', 'i']

text = input()

result = [x for x in text if x not in vowels]
print("".join(result))
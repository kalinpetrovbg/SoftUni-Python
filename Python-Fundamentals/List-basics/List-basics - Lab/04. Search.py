num = int(input())
keyword = input()

words = []
great_words = []

for x in range(num):
    new_word = input()
    words.append(new_word)
    if keyword in new_word:
        smart = new_word
        great_words.append(smart)

print(words)
print(great_words)
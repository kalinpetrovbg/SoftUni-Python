n = int(input())
result = {}
for _ in range(n):
    word = input()
    synonym = input()
    if word not in result:
        result[word] = []
    result[word].append(synonym)

for words, synonyms in result.items():
    print(f"{words} - {', '.join(synonyms)}")
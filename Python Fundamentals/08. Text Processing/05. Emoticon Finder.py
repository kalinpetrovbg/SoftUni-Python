# text = "There are so many emoticons nowadays :P I have many ideas :O what input to place here :)"
#
# for index, char in enumerate(text):
#     if char == ":":
#         emoticon = char + text[index + 1]
#         print(emoticon)


# text = input()
# for index in range(len(text)):
#     if text[index] == ":":
#         print(text[index: index + 2])


text = input()
for index in range(len(text)):
    if text[index] == ':':
        print(f'{text[index]}{text[index + 1]}')
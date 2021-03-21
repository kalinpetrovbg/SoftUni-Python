keys = [int(x) for x in input().split()]
text = input()

while text != "find":
    result = ""
    for index in range(len(text)):
        d = index % len(keys)
        letter = ord(text[index]) - keys[d]
        result += chr(letter)

    message = result[result.find("<")+1: result.find(">")]
    word = result[result.find("&")+1:]
    metal = word[:word.find("&")]
    print(f"Found {metal} at {message}")

    text = input()
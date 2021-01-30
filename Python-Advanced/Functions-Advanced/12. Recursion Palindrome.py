def palindrome(*args):
    keyword = args[0]
    for index in range(len(keyword) // 2):
        position = -(index + 1)
        if keyword[index] == keyword[position]:
            continue
        else:
            return f"{keyword} is not a palindrome"
    return f"{keyword} is a palindrome"

print(palindrome("abcba", 0))
print(palindrome("peter", 0))

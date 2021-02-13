words = input().split()
search = input()

palindroms = [x for x in words if x == x[:: -1]]

target = palindroms.count(search)

print(palindroms)
print(f"Found palindrome {target} times")
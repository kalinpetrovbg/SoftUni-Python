code = input().split(".")

code_in_int = int("".join(code)) + 1
code_in_str = str(code_in_int)

print(f"{code_in_str[0]}.{code_in_str[1]}.{code_in_str[2]}")


def validator(code):
    valid = 0
    let = 0
    if 6 <= len(code) <= 10:
        valid += 1
    else:
        print("Password must be between 6 and 10 characters")

    for letters in code:
        if letters.isalpha():
            let += 1
        if letters.isdigit():
            let += 1

    if len(code) == let:
        valid += 1
    else:
        print("Password must consist only of letters and digits")

    if len([x for x in code if x.isdigit()]) >= 2:  # less than 2 digits
        valid += 1
    else:
        print("Password must have at least 2 digits")

    if valid > 2:
        print("Password is valid")


validator(input())
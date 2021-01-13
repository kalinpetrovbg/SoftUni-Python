text = input().split(", ")
winners = "@#$^"

for tickets in text:
    ticket = tickets.strip()

    left_side = ticket[0:10]
    right_side = ticket[10:20]

    for char in winners:
        if char * 10 == left_side and char * 10 == right_side:
            print(f'ticket "{ticket}" - 10{char} Jackpot!')
            break

        if len(ticket) < 20:
            print('invalid ticket')
            break

        if char * 6 in left_side and char * 6 in right_side:
            min_left = left_side.count(char)
            min_right = right_side.count(char)
            print(f'ticket "{ticket}" - {min(min_left, min_right)}{char}')
            break

        # if char not in left_side and char not in right_side:
        #     print(f'ticket "{ticket}" - no match')
        #     break


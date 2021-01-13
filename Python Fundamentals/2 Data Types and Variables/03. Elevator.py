red_cards = input().split(" ")
team_a = 11
team_b = 11

for each in set(red_cards):
    if each[0] == "A":
        team_a -= 1
    if each[0] == "B":
        team_b -= 1
    if team_a < 7 or team_b < 7:
        break

print(f"Team A - {team_a}; Team B - {team_b}")
if team_a < 7 or team_b < 7:
    print("Game was terminated")
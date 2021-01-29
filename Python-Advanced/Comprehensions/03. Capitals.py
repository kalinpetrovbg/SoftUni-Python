countries = input().split(", ")
capitals = input().split(", ")

print(*[f"{countries[index]} -> {capitals[index]}" for index in range(len(countries))], sep="\n")
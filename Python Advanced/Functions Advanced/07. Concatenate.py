def concatenate(*args):
    result = [each for each in args]
    return "".join(result)

print(concatenate("Soft", "Uni", "Is", "Great", "!"))
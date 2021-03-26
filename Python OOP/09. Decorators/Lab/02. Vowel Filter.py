def vowel_filter(function):
    def wrapper():
        result = function()
        return [let for let in result if let in "aeouyi"]
    return wrapper

@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())

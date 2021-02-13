grade = float(input())


def grade_to_text():
    if 2 <= grade < 3:
        return "Fail"
    if 3 <= grade < 3.5:
        return "Poor"
    if 3.5 <= grade < 4.5:
        return "Good"
    if 4.5 <= grade < 5.5:
        return "Very Good"
    if 5.5 <= grade <= 6.0:
        return "Excellent"


print(grade_to_text())
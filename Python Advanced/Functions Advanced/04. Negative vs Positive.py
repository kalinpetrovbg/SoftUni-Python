def negative_vs_positive(nums):
    positive = sum(list(filter(lambda x: x > 0, nums)))
    negative = sum(list(filter(lambda x: x < 0, nums)))
    print(negative)
    print(positive)
    if positive > abs(negative):
        return "The positives are stronger than the negatives"
    else:
        return "The negatives are stronger than the positives"

numbers = [int(num) for num in input().split()]

print(negative_vs_positive(numbers))
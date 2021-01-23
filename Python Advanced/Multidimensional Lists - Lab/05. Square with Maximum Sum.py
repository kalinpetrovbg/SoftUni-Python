from itertools import chain

def read_matrix():
    row, col = [int(x) for x in input().split(", ")]
    matrix = [[int(x) for x in input().split(", ")] for _ in range(row)]
    return matrix

def get_squares(matrix):
    squares = []
    for i in range(len(matrix) - 1):
        row = matrix[i]
        for j in range(len(row) - 1):
            square = [
                [matrix[i][j], matrix[i][j + 1]],
                [matrix[i + 1][j], matrix[i + 1][j + 1]],
            ]
            squares.append(square)
    return squares

def get_sum_of_matrix(matrix):
    return sum(chain(*matrix))

def get_max_square(squares):
    max_square_sum = None
    max_square = None
    for square in squares:
        square_sum = get_sum_of_matrix(square)
        if max_square_sum is None or square_sum > max_square_sum:
            max_square_sum = square_sum
            max_square = square
    return max_square

matrix = read_matrix()
squares = get_squares(matrix)
max_square = get_max_square(squares)

print("\n".join([' '.join(map(str, x)) for x in max_square]))
print(get_sum_of_matrix(max_square))
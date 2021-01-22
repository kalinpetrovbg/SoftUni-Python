def read_matrix(is_test=False):
    if is_test:
        return [
            ['A', 'B', 'C'],
            ['D', 'E', 'F'],
            ['X', '!', '@'],
        ]
    else:
        size = int(input())
        matrix = []
        for row_index in range(size):
            row = [x for x in input()]
            matrix.append(row)

        return matrix


def find_symbol_in_matrix(matrix, symbol):
    for row_index in range(len(matrix)):
        if symbol in matrix[row_index]:
            return row_index, matrix[row_index].index(symbol)
        # for col_index in range(len(matrix[row_index])):
        #     current_symbol = matrix[row_index][col_index]
        #     if current_symbol == symbol:
        #         return (row_index, col_index)
    return None


def print_result(result, symbol):
    if result:
        print(result)
    else:
        print(f'{symbol} does not occur in the matrix')


matrix = read_matrix(is_test=True)
symbol = '1'

print_result(find_symbol_in_matrix(matrix, symbol), symbol)
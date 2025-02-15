

def f(row, col, board):

    if row==-1 or col==-1:
        return 0


    a = f(row-1, col, board)
    b = f(row, col-1, board)

    maxVal = max(a, b)

    return board[row][col] + maxVal


def fn(row, col, table, board):
    if table[row][col] != -1:
        return table[row][col]

    a = fn(row-1, col, board, table)
    b = fn(row, col-1, board, table)

    maxVal = max(a, b)

    table[row][col] = board[row][col] + maxVal




board = [[0, 1, 0, 0, 0, 0],  # table is 5 x 3 (0 indexed!)
         [0, 0, 1, 1, 1, 1],
         [1, 0, 0, 0, 1, 0],
         [0, 1, 0, 0, 0, 1],
         ]




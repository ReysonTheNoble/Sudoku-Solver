import pprint


def solve(game_board):

    """
    Solves a sudoku board using a backtracking algorithm
    :param game_board: 2D array of ints
    :return: solution
    """
    empty = find_empty(game_board)
    if empty:
        row, col = empty
    else:
        return True

    for i in range(1,10):
        if valid(game_board, (row, col), i):
            game_board[row][col] = i

            if solve(game_board):
                return True

            game_board[row][col] = 0

    return False

def valid(game_board, pos, num):
    """
    :param game_board: 2D array of ints
    :param pos: (row, col)
    :param num: int
    :return: bool
    """

    # Check row
    for i in range(0, len(game_board)):
        if game_board[pos[0]][i] == num and pos[1] != i:
            return False

    # Check col
    for i in range(0, len(game_board)):
        if game_board[i][pos[1]] == num and pos[1] != i:
            return False

    # Check box
    box_x = pos[1]//3
    box_y = pos[0]//3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if game_board[i][j] == num and (i,j) != pos:
                return False

    return True

def find_empty(game_board):
    """
    finds an empty space on the board
    :param game_board: partially complete board
    :return: (int, int) row, col
    """

    for i in range(len(game_board)):
        for j in range(len(game_board[0])):
            if game_board[i][j] == 0:
                return i, j

    return None

def print_board(game_board):
    """
    function to print the board
    :param game_board: 2D Array of ints
    :return: None
    """
    for i in range(len(game_board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - -")
        for j in range(len(game_board[0])):
            if j % 3 == 0:
                print(" | ", end="")

            if j == 8:
                print(game_board[i][j], end="\n")
            else:
                print(str(game_board[i][j]) + " ", end="")

board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

pp = pprint.PrettyPrinter(width=41, compact=True)
solve(board)
pp.pprint(board)

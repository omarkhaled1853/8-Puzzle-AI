from puzzle_solver.a_star import *
from puzzle_solver.utils import *


def convert_board_to_int(board):
    new_board = 0
    for i in board:
        new_board *= 10
        new_board += i
    return new_board


def convert_int_to_board(board):
    new_board = [0] * 9
    i = 8
    while board:
        new_board[i] = board % 10
        board //= 10
        i -= 1
    return new_board


def print_output(output):
    for step in output:
        cur_board = convert_int_to_board(step)
        for i in range(0, 9, 3):
            print(cur_board[i:i + 3])
        print('='*30)


def main():
    # board = [1, 2, 5, 3, 4, 0, 6, 7, 8]
    board = [1, 3, 0, 6, 7, 2, 5, 4, 8]
    # board = [5, 3, 1, 4, 2, 8, 7, 6, 0]
    # board = [0, 4, 2, 5, 3, 7, 1, 8, 6]
    # board = [3, 1, 2, 6, 4, 5, 7, 8, 0]
    new_board = convert_board_to_int(board)
    solver = A_Star(new_board, manhattan_distance)
    res = solver.solve()

    print_output(res)
    print("MOVES:", len(res) - 1)


if __name__ == '__main__':
    main()

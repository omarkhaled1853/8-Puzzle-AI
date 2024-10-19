from puzzle_solver.a_star import *
from puzzle_solver.utils import *


def print_output(output):
    for step in output:
        for i in range(0, 9, 3):
            print(step[i:i + 3])
        print('='*30)


def main():
    # board = [1, 2, 5, 3, 4, 0, 6, 7, 8]
    # board = [1, 3, 0, 6, 7, 2, 5, 4, 8]
    board = [5, 3, 1, 4, 2, 8, 7, 6, 0]
    # board = [0, 4, 2, 5, 3, 7, 1, 8, 6]
    solver = A_Star(board, manhattan_distance)
    res = solver.solve()

    print_output(res)
    print("MOVES:", len(res) - 1)


if __name__ == '__main__':
    main()

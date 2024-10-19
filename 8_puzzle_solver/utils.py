
from typing import List


def manhattan_distance(board: List[int]) -> int:
    """
    Calculates the manhattan distance for a given board.
    returns the distance.
    """
    cost = 0
    for i in range(len(board)):
        true_x, true_y = i // 3, i % 3
        cur_x, cur_y = board[i] // 3, board[i] % 3

        cost += abs(true_x - cur_x) + abs(true_y - cur_y)

    return cost

def euclidean_distance(board: List[int]) -> float:
    """
    Calculates the Euclidean distance for a given board.
    returns the distance.
    """
    cost = 0
    for i in range(len(board)):
        true_x, true_y = i // 3, i % 3
        cur_x, cur_y = board[i] // 3, board[i] % 3

        cost += ((true_x - cur_x) ** 2 + (true_y - cur_y) ** 2) ** 0.5

    return cost
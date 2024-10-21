
from typing import List


def manhattan_distance(board: int) -> int:
    """
    Calculates the manhattan distance for a given board.
    returns the distance.
    """
    cost = 0
    for i in range(9):
        tile = (board // (10 ** i)) % 10  # Extracft the current tile
        if tile == 0:  # Skip the empty tile
            continue

        # True position: tile
        true_x, true_y = tile // 3, tile % 3
        # Current position: 8 - i
        cur_x, cur_y = (8 - i) // 3, (8 - i) % 3

        cost += abs(true_x - cur_x) + abs(true_y - cur_y)

    return cost


def euclidean_distance(board: int) -> float:
    """
    Calculates the Euclidean distance for a given board.
    returns the distance.
    """
    cost = 0
    for i in range(9):
        tile = (board // (10 ** i)) % 10  # Extracft the current tile
        if tile == 0:  # Skip the empty tile
            continue

        # True position: tile
        true_x, true_y = tile // 3, tile % 3
        # Current position: 8 - i
        cur_x, cur_y = (8 - i) // 3, (8 - i) % 3

        cost += ((true_x - cur_x) ** 2 + (true_y - cur_y) ** 2) ** 0.5

    return cost

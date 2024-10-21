from typing import List


class State:
    def __init__(self, board: int, empty_tile: int, parent=None, g_n: int = 0, h_n: float = 0) -> None:
        self.board: int = board
        self.parent: State = parent
        self.empty_tile: int = empty_tile
        self.g_n: int = g_n
        self.h_n: float = h_n

    def get_path(self) -> List[int]:
        path = []
        cur_state: State = self

        while cur_state:
            path.append(cur_state.board)
            cur_state = cur_state.parent

        return path[::-1]

    def __hash__(self) -> int:
        return hash(self.board)

    def __eq__(self, other) -> bool:
        return self.board == other.board

    def __lt__(self, other):
        return self.g_n + self.h_n < other.g_n + other.h_n

    def __gt__(self, other):
        return self.g_n + self.h_n > other.g_n + other.h_n

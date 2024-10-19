from typing import List


class State:
    def __init__(self, board: List[int], parent=None, g_n: int = 0, h_n: int = 0) -> None:
        self.board = board
        self.parent = parent
        self.g_n = g_n
        self.h_n = h_n

    def get_path(self):
        path = []
        cur_state: State = self

        while cur_state:
            path.append(cur_state.board)
            cur_state = cur_state.parent

        return path[::-1]

    def __hash__(self) -> int:
        return hash(str(self.board))

    def __eq__(self, other) -> bool:
        return self.board == other.board

    def __lt__(self, other):
        return self.g_n + self.h_n < other.g_n + other.h_n

    def __gt__(self, other):
        return self.g_n + self.h_n > other.g_n + other.h_n

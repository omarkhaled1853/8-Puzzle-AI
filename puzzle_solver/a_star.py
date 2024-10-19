import heapq
from typing import List
from .state import State


class A_Star:
    def __init__(self, board: List[int], heuristic) -> None:
        self.board = board
        self.heuristic = heuristic
        self.dirs = [
            -1,  # Left
            1,  # Right
            -3,  # Up
            3   # Down
        ]

    def is_solved(self, state: State) -> bool:
        return state.board == [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def solve(self):
        initial_state = State(board=self.board)
        visited = set()
        # g(n) is number of moves. h(n) heuristic estimate
        frontier = []  # Heap (g(n) + h(n), g(n), state).

        # heapq.heappush(frontier, (0, 0, initial_state))
        heapq.heappush(frontier, initial_state)

        while frontier:
            # f_n, g_n, state = heapq.heappop(frontier)
            state = heapq.heappop(frontier)

            if self.is_solved(state):
                return state.get_path()

            visited.add(state)

            empty_tile = self.get_empty_tile(state.board)
            for dir in self.dirs:
                if self.is_valid_tile(empty_tile, empty_tile + dir):
                    new_empty_tile = empty_tile + dir
                    new_board = state.board.copy()
                    new_board[empty_tile], new_board[new_empty_tile] = new_board[new_empty_tile], new_board[empty_tile]
                    new_state = State(new_board, state)

                    if new_state not in visited:
                        h_n = self.heuristic(new_board)
                        # cost = g_n + 1 + h_n
                        new_state.g_n = state.g_n + 1
                        new_state.h_n = h_n
                        # heapq.heappush(frontier, (cost, g_n + 1, new_state))
                        heapq.heappush(frontier, new_state)

        return None

    def is_valid_tile(self, before, after):
        if after < 0 or after >= 9:
            return False
        if abs(before - after) == 1 and (before // 3) != (after // 3):
            return False
        return True

    def get_empty_tile(self, board: List[int]) -> int:
        return board.index(0)

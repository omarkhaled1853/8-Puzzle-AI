from typing import List, Type


class State:
    def __init__(self, board: List[int], parent: State = None) -> None:
        self.board = board
        self.parent = parent
    
    def get_path(self):
        path = []
        cur_state: State = self

        while cur_state:
            path.append(cur_state.board)
            cur_state = cur_state.parent
        
        return path[::-1]
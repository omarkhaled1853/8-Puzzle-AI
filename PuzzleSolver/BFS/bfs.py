from queue import Queue
from PuzzleSolver.BFS.node import *
from PuzzleSolver.search import *

class BFS(Search):
    # list of the possible movement directions
                # up    down    right   left
    __dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    
    # get empty tile location
    def __get_empty_tile_location(self, board) -> int:
        idx = 8
        while board % 10:
            board //= 10
            idx -= 1
        return idx
        
    # mapping 1D location of empty tile into 2D location (row, column)
    def __convert_to_row_column(self, location: int) -> tuple[int]:
        return location // 3, location % 3
    
    # mapping 2D location of empty tile into 1D location (index)
    def __convert_to_index(self, location: tuple[int], dir) -> int:
        return (location[0] + dir[0]) * 3 + (location[1] + dir[1])
    
    # function check boundary condition of puzzle board
    def __is_safe(self, location: tuple[int], dir) -> bool:
        return location[0] + dir[0] >= 0 and location[0] + dir[0] < 3 and location[1] + dir[1] >= 0 and location[1] + dir[1] < 3

    # function check reaching goal
    def __is_solved(self, board):
        return board == 12345678
    
    # get value of location in board
    def __get_value(self, board, location):
        # print(location)
        location = 8 - location
        while location:
            board //= 10
            location -= 1
        return board % 10

    # get new board
    def __get_new_board(self, board, old_location, new_location):
        value = self.__get_value(board, new_location)
        # print(value)
        return board - (value * 10 ** (8 - new_location)) + (value * 10 ** (8 - old_location))

    # get movment of empty tile
    def __get_movement(self, dir):
        idx = self.__dirs.index(dir)
        if (idx == 0): return 'UP'
        elif (idx == 1): return 'DOWN'
        elif (idx == 2): return 'RIGHT'
        else: return  'LEFT'


    # get path from root to the goal
    def __get_path(self, root: Node):
        path = []
        while root:
            path.append(root.get_board())
            root = root.get_parent()
        return path[::-1]
    
    # get movements from root to goal 
    def __get_movements(self, root: Node):
        movements = []
        while root:
            movements.append(root.get_movement())
            root = root.get_parent()
        movements.pop()
        return movements[::-1]
        

    # bfs algorithm that take the intial puzzle, intial localtion of the empty tile
    # and the goal that interest to reach 
    # then return the path, frontier queue (if any) and expanded set
    def solve(self) -> dict:
        # get empty tile location in the intial state
        intial_empty_tile_location = self.__get_empty_tile_location(self._intial_state)

        # create a root node with its intial value of the puzzle and empty tile location 
        root = Node(self._intial_state, intial_empty_tile_location)
        
        # frontier queue to keep track with the interesting nodes and movment of empty tile
        frontier = Queue()
        frontier.put(root)
        # visited set to keep track with the visited nodes (can be not processed)
        visited = {root}
        # expanded set to keep track with the visited and processed nodes
        expanded = set()
        # keep track with max depth search
        max_depth_search = 0

        # loop until frontier queue becomes empty
        while frontier:
            # get the current interesting node
            node: Node = frontier.get()
            # add the interesting node in expanded set
            expanded.add(node)

            node_board = node.get_board()

            # check reaching the goal 
            if self.__is_solved(node_board):
                path = self.__get_path(node)
                # return dictionary of needed values
                return {
                    'path_to_goal': self.__get_movements(node),
                    'cost_of_path': len(path) - 1,
                    'nodes_expanded': len(expanded),
                    'search_depth': max_depth_search,
                    'goal_steps': path[1:]
                }
            
            # searching up, down, right, and left for the next movment of the empty tile
            for dir in self.__dirs:
                old_empty = node.get_empty_tile_location()
                # convert from 1D to 2D
                old_empty_row_column = self.__convert_to_row_column(old_empty)

                # check if not out of bound of the puzzle board
                if(self.__is_safe(old_empty_row_column, dir)):
                    # get new emptiy tile location
                    new_empty = self.__convert_to_index(old_empty_row_column, dir)

                    # get new board with new empty tile location
                    new_board = self.__get_new_board(node_board, old_empty, new_empty)

                    # get movement of the empty tile
                    movement = self.__get_movement(dir)

                    # create new node
                    new_node = Node(new_board, new_empty, node, movement)
                    
                    # update max depth search
                    max_depth_search = max(max_depth_search, new_node.get_depth())

                    # check if the new searched board is exist in visited set before
                    if new_node not in visited:
                        visited.add(new_node)
                        frontier.put(new_node)
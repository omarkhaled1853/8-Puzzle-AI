import copy
from queue import Queue
from node import Node


class BFS:
    # list of the possible movement directions
    #           up   down   right   left 
    __dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    def __init__(self, intial_state: list[int]) -> None:
        self.__intial_state = intial_state
    
    # get empty tile location
    def __get_empty_tile_location(self) -> tuple:
        for i in range(3):
            for j in range(3):
                if(self.__intial_state[i][j] == 0):
                    return (i, j)
                
    # function check boundary condition of puzzle board
    def __is_safe(self, x, y):
        return x >= 0 and x < 3 and y >= 0 and y < 3
    
    # function check reaching goal
    def __is_solved(self, board):
        return board == [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8]
        ]
    
    # get movment of empty tile
    def __get_movement(self, dir):
        idx = self.__dirs.index(dir)
        if (idx == 0): return 'UP'
        elif (idx == 1): return 'DOWN'
        elif (idx == 2): return 'RIGHT'
        else: return  'LEFT'


    # get path from root to the goal
    def __get_path_and_movments(self, root: Node):
        path = []
        movements = []
        while root:
            path.append(root.get_board())
            movements.append(root.get_movement())
            root = root.get_parent()
        movements.pop()
        return path[::-1], movements[::-1]
        

    # bfs algorithm that take the intial puzzle, intial localtion of the empty tile
    # and the goal that interest to reach 
    # then return the path, frontier queue (if any) and expanded set
    def solve(self):
        # get empty tile location in the intial state
        intial_empty_tile_location = self.__get_empty_tile_location()

        # create a root node with its intial value of the puzzle and empty tile location 
        root = Node(self.__intial_state, intial_empty_tile_location)
        
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
                path, movements = self.__get_path_and_movments(node)
                cost = len(path) - 1
                number_of_expanded_nodes = len(expanded)
                return movements, cost, number_of_expanded_nodes, max_depth_search, path
            
            # searching up, down, right, and left for the next movment of the empty tile
            for dir in self.__dirs:
                old_empty = node.get_empty_tile_location()
                new_empty = (old_empty[0] + dir[0], old_empty[1] + dir[1])

                # check if not out of bound of the puzzle board
                if(self.__is_safe(new_empty[0], new_empty[1])):
                    new_board = copy.deepcopy(node_board)

                    new_board[old_empty[0]][old_empty[1]], new_board[new_empty[0]][new_empty[1]] = (
                        new_board[new_empty[0]][new_empty[1]],
                        0,
                    )
                    # get movement of the empty tile
                    movement = self.__get_movement(dir)

                    new_node = Node(new_board, new_empty, node, movement)
                    # update max depth search
                    max_depth_search = max(max_depth_search, new_node.get_depth())

                    # check if the new searched board is exist in visited set before
                    if new_node not in visited:
                        visited.add(new_node)
                        frontier.put(new_node)
import copy
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


    # get path from root to the goal
    def __get_path(self, root: Node, path: list):
        if root == None:
            return
        self.__get_path(root.get_parent(), path)
        path.append(root.get_board())

    # bfs algorithm that take the intial puzzle, intial localtion of the empty tile
    # and the goal that interest to reach 
    # then return the path, frontier queue (if any) and expanded set
    def solve(self):
        # get empty tile location in the intial state
        intial_empty_tile_location = self.__get_empty_tile_location()

        # create a root node with its intial value of the puzzle and empty tile location 
        root = Node(None, self.__intial_state, intial_empty_tile_location)
        
        # frontier queue to keep track with the interesting nodes
        frontier = [root]
        # expanded set to keep track with the visited and progressed nodes
        expanded = []

        # loop until frontier queue becomes empty
        while frontier:
            # get the current interesting node
            node = frontier.pop(0)
            # add the interesting node in expanded set
            expanded.append(node)

            node_board = node.get_board()
            
            # check reaching the goal 
            if self.__is_solved(node_board):
                path = []
                self.__get_path(node, path)
                return path, frontier, expanded
            
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
                    new_node = Node(node, new_board, new_empty)

                    # check if the new searched board is exist in frontier queue or expanede set before
                    if not any(n.get_board() == new_board for n in frontier + expanded):
                        frontier.append(new_node)

                
# ======================================================================================================================
# example
board = [
    [1, 2, 5],
    [3, 4, 0],
    [6, 7, 8]
]

bfs = BFS(board)

# perform BFS algorithm
path, frontier, expanded = bfs.solve()

# printing path for reaching the goal
print(f'Path to the goal:')
for arr in path:
    for r in arr:
        print(r)
    print('*'*100)

print("="*100)

# printing number of visited nodes and the visited nodes itself 
print(f'Number of expanded nodes: {len(expanded)}')
print(f'Expanded nodes:')
for node in expanded:
    print(node.get_empty_tile_location())
    for r in node.get_board():
        print(r)
    print('*'*100)

print("="*100)

# printing number of in progressed nodes but not visited and the progressed nodes itself 
print(f'Number of not expanded nodes: {len(frontier)}')
print(f'Not expanded nodes:')
for node in frontier:
    print(node.get_empty_tile_location())
    for r in node.get_board():
        print(r)
    print('*'*100)
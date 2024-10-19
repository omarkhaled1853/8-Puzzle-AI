import copy

# encapsulated node class
class Node:
    def __init__(self, parent, board, empty_tile_location) -> None:
        # puzzle board
        self.__board = board
        # parent node of the current node
        self.__parent = parent
        # tuble of the empty tile location
        self.__empty_tile_location = empty_tile_location
    
    def get_parent(self):
        return self.__parent

    def get_board(self):
        return self.__board

    def get_empty_tile_location(self):
        return self.__empty_tile_location


# get path from root to the goal
def get_path(root, path):
    if root == None:
        return
    get_path(root.get_parent(), path)
    path.append(root.get_board())


# function check boundary condition of puzzle board
def is_safe(x, y):
    return x >= 0 and x < 3 and y >= 0 and y < 3


# list of the possible movement directions
#           up   down   right   left 
dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]


# bfs algorithm that take the intial puzzle, intial localtion of the empty tile
# and the goal that interest to reach 
# then return the path, frontier queue (if any) and expanded set
def BFS(intial_state, intial_empty_tile_location, goal):
    # create a root node with its intial value of the puzzle and empty tile location 
    root = Node(None, intial_state, intial_empty_tile_location)
    
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
        if node_board == goal:
            path = []
            get_path(node, path)
            return path, frontier, expanded
        
        # searching up, down, right, and left for the next movment of the empty tile
        for dir in dirs:
            old_empty = node.get_empty_tile_location()
            new_empty = (old_empty[0] + dir[0], old_empty[1] + dir[1])

            # check if not out of bound of the puzzle board
            if(is_safe(new_empty[0], new_empty[1])):
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

goal = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]

# perform BFS algorithm
path, frontier, expanded = BFS(board, (1, 2), goal)

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
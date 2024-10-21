# encapsulated node class
class Node:
    def __init__(self, board, empty_tile_location, parent = None, movement:str = None) -> None:
        # puzzle board
        self.__board = board
        # parent node of the current node
        self.__parent = parent
        # tuble of the empty tile location
        self.__empty_tile_location = empty_tile_location
        # movment of the node
        self.__movement = movement
        # Depth = parent depth + 1
        self.__depth = parent.__depth + 1 if parent else 0  
    
    def get_parent(self):
        return self.__parent

    def get_board(self):
        return self.__board

    def get_empty_tile_location(self) -> tuple[int]:
        return self.__empty_tile_location
    
    def get_movement(self) -> str:
        return self.__movement

    def get_depth(self) -> int:
        return self.__depth
    
    # hash board value
    def __hash__(self) -> int:
        return hash(tuple(map(tuple, self.__board)))
    
    def __eq__(self, other) -> bool:
        if isinstance(other, Node):
            return self.__board == other.__board
        return False
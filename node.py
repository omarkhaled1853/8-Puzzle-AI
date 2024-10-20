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
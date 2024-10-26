import math


class Heuristics:
    goal = "012345678"

    def Manhattan_Distance(self, board: int) -> int:
        board = str(board)
        if len(board) == 8:
            board = '0' + board  # append 0 if the board start with 0: 31265478

        distance = 0
        for index, char in enumerate(board):
            if char == '0':  # We do not calculate the empty node distance
                continue

            current_cell_x = index // 3
            current_cell_y = index % 3

            cell_index = self.goal.index(char)
            goal_x = cell_index // 3
            goal_y = cell_index % 3

            distance += abs(current_cell_x - goal_x) + abs(current_cell_y - goal_y)

        return distance

    def Euclidean_Distance(self, board: int) -> float:  # Return float not int because the function contain square root
        board = str(board)
        if len(board) == 8:
            board = '0' + board

        distance = 0
        for index, char in enumerate(board):
            if char == '0':  # We do not calculate the empty node distance
                continue

            current_cell_x = index // 3
            current_cell_y = index % 3

            cell_index = self.goal.index(char)
            goal_x = cell_index // 3
            goal_y = cell_index % 3

            distance += math.sqrt((current_cell_x - goal_x) ** 2 + (current_cell_y - goal_y) ** 2)

        return distance


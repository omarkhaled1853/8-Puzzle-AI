import heapq


class A_Star:

    def __init__(self, board: int, heuristic) -> None:  # initial state and heuristic function
        self.board = board
        self.heuristic = heuristic

    def goal_test(self, board: int) -> bool:
        return board == 12345678

    def validState(self, emptyPos, newPos):
        if newPos < 0 or newPos >= 9:
            return False

        return (emptyPos % 3 == newPos % 3) or (emptyPos // 3 == newPos // 3)

    def getNeighbors(self, state: str):
        if len(state) == 8:
            state = '0' + state

        # Right, Left, Down, Up
        directions = [1, -1, 3, -3]
        emptyPos = state.index('0')

        neighbors = []
        for direction in directions:
            newPos = emptyPos + direction
            if self.validState(emptyPos, newPos):
                newState = list(state)
                newState[newPos], newState[emptyPos] = newState[emptyPos], newState[newPos]
                neighbors.append(int(''.join(newState)))

        return neighbors

    def in_frontier(self, frontier: heapq, state: int) -> bool:
        for item in frontier:
            if item[2] == state:
                return True

        return False

    def decrease_key(self, frontier: heapq, board: int, new_h, new_g) -> bool:
        nodes = []  # temporary list

        lower_key = False
        while frontier:
            estimate, g, state = heapq.heappop(frontier)

            if state == board:
                if new_h + new_g < estimate:
                    lower_key = True
                    estimate = new_h + new_g
                    g = new_g

            nodes.append((estimate, g, state))

        for node in nodes:
            heapq.heappush(frontier, node)

        return lower_key

    def solve(self) -> dict:
        frontier = []
        h_root = self.heuristic(self.board)
        heapq.heappush(frontier, (h_root + 0, 0, self.board))  # insert (h+g, g, initial_state)

        parent = {self.board: -1}
        explored = set()
        max_depth = 0

        path_found = False

        while frontier:
            estimate, g, state = heapq.heappop(frontier)
            explored.add(state)
            max_depth = max(max_depth, g)

            if self.goal_test(state):
                path_found = True
                break

            neighbors = self.getNeighbors(str(state))

            for neighbor in neighbors:
                if neighbor not in explored:
                    node_h = self.heuristic(neighbor)
                    node_g = g + 1

                    if self.in_frontier(frontier, neighbor):
                        if self.decrease_key(frontier, neighbor, node_h, node_g):  # decrease key if new key is lower
                            parent[neighbor] = state  # update the neighbor to the new parent
                    else:
                        heapq.heappush(frontier, (node_h + node_g, node_g, neighbor))
                        parent[neighbor] = state

        if path_found:
            path = self.getGoalPath(parent, goal=12345678)
            return self.getResultInformation(path, len(explored), max_depth)

    def getResultInformation(self, path: list, nodes_expanded: int, max_depth: int) -> dict:
        path_to_goal = [item[0] for item in path]
        goal_steps = [item[1] for item in path]

        result_information = {'path_to_goal': path_to_goal,
                              'cost_of_path': len(path_to_goal),
                              'nodes_expanded': nodes_expanded,
                              'search_depth': max_depth,
                              'goal_steps': goal_steps
                              }

        return result_information

    # Function that return the goal path, return the state and the direction to this state
    def getGoalPath(self, parents, goal) -> list:
        current_state = goal
        parent = parents[current_state]

        resultDirections = []
        while parent != -1:
            resultDirections.append((self.getDirection(current_state, parent), current_state))
            current_state = parent
            parent = parents[parent]

        return list(reversed(resultDirections))

    # Function to get the direction move between to state, it is return left or right or up or down
    def getDirection(self, current_state, parent) -> str:
        neighbors = self.getNeighborsWithDirections(str(parent))

        for neighbor, direction in neighbors:
            if neighbor == current_state:
                return direction

    def getNeighborsWithDirections(self, state: str) -> list:
        if len(state) == 8:
            state = '0' + state

        # Right, Left, Down, Up
        directions = [
            (1, 'right'),
            (-1, 'left'),
            (3, 'down'),
            (-3, 'up')
        ]
        emptyPos = state.index('0')

        neighbors = []
        for direction, move in directions:
            newPos = emptyPos + direction
            if self.validState(emptyPos, newPos):
                newState = list(state)
                newState[newPos], newState[emptyPos] = newState[emptyPos], newState[newPos]
                neighbors.append((int(''.join(newState)), move))

        return neighbors

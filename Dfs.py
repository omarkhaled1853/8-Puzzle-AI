
class DFS:
    parent = []
    frontier = []
    explored = set()
    depth = []
    max_depth = 0
    goal = 12345678

    def __init__(self, intial_state, limit = None) -> None:
        self.__intial_state = intial_state
        self.__limit = limit

    def validState(self, emptyPos, newPos):
        if newPos < 0 or newPos >= 9:
            return False
        if (emptyPos % 3 == 0 and newPos == emptyPos - 1) or (emptyPos % 3 == 2 and newPos == emptyPos + 1):
            return False  # Prevent wrapping around rows
        return True

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

    def getNeighborsWithDirections(self, state: str):
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

    # Function to get the direction move between to state, it is return left or right or up or down
    def getDirection(self, current_state, parent):
        neighbors = self.getNeighborsWithDirections(str(parent))

        for neighbor, direction in neighbors:
            if neighbor == current_state:
                return direction

    # Function that return the goal path, return the state and the direction to this state
    def getGoalPath(self, parentList, goal):
        current_state = goal
        parent = parentList[current_state]

        resultDirections = []
        while parent != -1:
            resultDirections.append((self.getDirection(current_state, parent), current_state))
            current_state = parent
            parent = parentList[parent]

        return list(reversed(resultDirections))

    def getResultInformation(self):
        path = self.getGoalPath(self.parent, self.goal)
        path_to_goal = [item[0] for item in path]
        goal_steps = [item[1] for item in path]

        result_information = {'path_to_goal': path_to_goal,
                              'cost_of_path': len(path_to_goal),
                              'nodes_expanded': len(self.explored),
                              'search_depth': self.max_depth,
                              'goal_steps': goal_steps
                              }
        return result_information

    def dfs(self, limit=float('inf')):
        """Performs DFS with an optional depth limit."""
        while len(self.frontier) != 0:

            state = self.frontier.pop()
            self.explored.add(state)
            self.max_depth = max(self.max_depth, self.depth[state])

            if state == self.goal:
                return True

            # Skip deeper exploration if the limit is reached.
            if self.depth[state] >= limit:
                continue

            neighbors = self.getNeighbors(str(state))

            for neighbor in neighbors:
                if neighbor not in self.explored and neighbor not in self.frontier:
                    self.frontier.append(neighbor)
                    self.parent[neighbor] = state
                    self.depth[neighbor] = self.depth[state] + 1

        return False

    def solve(self):
        """Solves using DFS if no limit, otherwise IDFS."""
        # Set search parameters.
        self.parent = {self.__intial_state: -1}
        self.frontier = [self.__intial_state]
        self.explored = set()
        self.max_depth = 0
        self.depth = {self.__intial_state: 0}

        # If a limit is provided, run IDFS by gradually increasing the depth.
        if self.__limit is not None:
            for i in range(self.__limit + 1):
                self.reset_state()
                if self.dfs(i):
                    return self.getResultInformation()
        else:  # Otherwise, just perform regular DFS.
            if self.dfs():
                return self.getResultInformation()

    def reset_state(self):
        """Resets the search state for each new depth limit in IDFS."""
        self.parent = {self.__intial_state: -1}
        self.frontier = [self.__intial_state]
        self.explored = set()
        self.max_depth = 0
        self.depth = {self.__intial_state: 0}


dfs = DFS(125340678)
res1 = dfs.solve()

print(res1['path_to_goal'])
print(res1['cost_of_path'])
print(res1['nodes_expanded'])
print(res1['search_depth'])
print(res1['goal_steps'])

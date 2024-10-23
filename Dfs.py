import time


class DfsPuzzle:
    parent = []
    frontier = []
    explored = set()
    depth = []
    max_depth = 0
    elapsed_time = 0
    goal = 12345678

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
                              'running_time': self.elapsed_time,
                              'goal_steps': goal_steps
                              }
        return result_information


class IterativeDeepSearch(DfsPuzzle):
    def dfs(self, limit):
        while len(self.frontier) != 0:

            state = self.frontier.pop()
            self.explored.add(state)
            self.max_depth = max(self.max_depth, self.depth[state])

            if state == self.goal:
                return True

            if self.depth[state] == limit:
                continue

            neighbors = self.getNeighbors(str(state))

            for neighbor in neighbors:
                if (neighbor not in self.explored) and (neighbor not in self.frontier):
                    self.frontier.append(neighbor)
                    self.parent[neighbor] = state
                    self.depth[neighbor] = self.depth[state] + 1

        return False

    def solve(self, initialState, limit):
        for i in range(limit + 1):
            self.parent = {initialState: -1}
            self.frontier = [initialState]
            self.explored = set()
            self.max_depth = 0
            self.depth = {initialState: 0}

            time_start = time.time()
            findSolution = self.dfs(i)
            time_end = time.time()

            self.elapsed_time = time_end - time_start

            if findSolution:
                return self.getResultInformation()


class Dfs(DfsPuzzle):
    # Iterative dfs function
    def dfs(self):
        while len(self.frontier) != 0:

            state = self.frontier.pop()
            self.explored.add(state)
            self.max_depth = max(self.max_depth, self.depth[state])

            if state == self.goal:
                return True

            neighbors = self.getNeighbors(str(state))

            for neighbor in neighbors:
                if (neighbor not in self.explored) and (neighbor not in self.frontier):
                    self.frontier.append(neighbor)
                    self.parent[neighbor] = state
                    self.depth[neighbor] = self.depth[state] + 1

        return False

    def solve(self, initialState):
        self.parent = {initialState: -1}
        self.frontier = [initialState]
        self.explored = set()
        self.max_depth = 0
        self.depth = {initialState: 0}

        time_start = time.time()
        findSolution = self.dfs()
        time_end = time.time()

        self.elapsed_time = time_end - time_start

        if findSolution:
            return self.getResultInformation()


dfsMethodIterative = IterativeDeepSearch()
res1 = dfsMethodIterative.solve(initialState=125340678, limit=3)

dfsMethod = Dfs()
res2 = dfsMethod.solve(initialState=125340678)

print(res1['path_to_goal'])
print(res1['cost_of_path'])
print(res1['nodes_expanded'])
print(res1['search_depth'])
print(res1['running_time'])
print(res1['goal_steps'''])

print()

print(res2['path_to_goal'])
print(res2['cost_of_path'])
print(res2['nodes_expanded'])
print(res2['search_depth'])
print(res2['running_time'])
print(res2['goal_steps'''])

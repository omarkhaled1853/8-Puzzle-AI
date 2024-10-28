# 8-Puzzle Game with GUI Solver

This is an interactive **8-Puzzle game** with a graphical user interface (GUI). The solver supports multiple search algorithms like **BFS, DFS, IDFS, A\*** with configurable heuristics. Users can input their custom puzzle or generate a random one and visualize the solution step-by-step using **Next** and **Previous** buttons.

## Features

- **Algorithms supported**:
  - **Breadth-First Search (BFS)**
  - **Depth-First Search (DFS)**
  - **Iterative Deepening DFS (IDFS)**
  - **A\*** with two heuristics:
    - **Manhattan Distance**
    - **Euclidean Distance**
  
- **Custom Puzzle Input**: Users can manually input the puzzle's starting state.
- **Random Puzzle Generator**: Create a random valid 8-puzzle configuration with one click.
- **Solution Visualization**:
  - Navigate through the solution with **Next** and **Previous** buttons.
  - View details about each solution step, including the number of moves and visited nodes.
- **Adjustable Limits**: Set a depth limit for IDFS.

- ## Usage

1. **Board Setup**:
   - **Manual Input**:  
     Enter the starting state by filling in the puzzle grid with numbers from 0 to 8, where `0` represents the empty tile.
   - **Random Board**:  
     Generate a random valid starting board by clicking the **"Randomize"** button.

2. **Select Algorithm**:
   - Choose one of the following algorithms:
     - **BFS** (Breadth-First Search)
     - **DFS** (Depth-First Search)
     - **IDFS** (Iterative Deepening DFS)  
       - If using **IDFS**, set the **depth limit** using the input field.
     - **A\*** (A-star Search)  
       - If using A\*, select one of the two heuristics:
         - **Manhattan Distance**
         - **Euclidean Distance**

3. **Solve the Puzzle**:
   - Click the **"Solve"** button to find the solution.
   - If a solution exists, you will be able to view it step-by-step.

4. **Solution Navigation**:
   - Use the **Next** button to move forward through the solution.
   - Use the **Previous** button to move backward.

5. **View Solution Details**:
   - The following statistics will be displayed:
     - **Path to Goal**: Total movements to reach goal.
     - **Nodes Expanded**: Total number of nodes visited during the search.
     - **Cost of Path**: The total cost to reach the goal state.
     - **Search Depth**: Maximum depth reached when searching



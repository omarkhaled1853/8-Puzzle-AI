from BuzzleSolver.BFS.bfs import *
from BuzzleSolver.DFS.dfs import *
from BuzzleSolver.factory import *
from BuzzleSolver.A_star.a_star import *
from BuzzleSolver.A_star.heuristic import *
import time

def main():
    # example
    board = 125340678

    heu = Heuristics()
    a_star = Factory.get_technique('A_star', intial_state=board, heuristic=heu.Euclidean_Distance)

    # perform BFS algorithm
    start = time.time()
    output = a_star.solve()
    end = time.time()

    print(f'time: {(end - start) * 1000} ms')
    print('path_to_goal:',output['path_to_goal'])
    print('cost_of_path:',output['cost_of_path'])
    print('nodes_expanded:',output['nodes_expanded'])
    print('search_depth:',output['search_depth'])
    print('path:', output['goal_steps'])

if __name__ == '__main__':
    main()
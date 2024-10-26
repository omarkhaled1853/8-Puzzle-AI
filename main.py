from BuzzleSolver.BFS.bfs import *
from BuzzleSolver.DFS.dfs import *
from BuzzleSolver.algorithm_factory import *
from BuzzleSolver.A_star.a_star import *
from BuzzleSolver.A_star.heuristic_factory import *
import time

def main():
    # example
    board = 125340678

    heu = Heuristic_Factory.get_heuristic('Manhattan')
    a_star = Algorithm_Factory.get_technique('A*', intial_state=board, heuristic=heu)

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
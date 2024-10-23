from bfs import BFS
import time

def main():
    # example
    board = 125340678

    bfs = BFS(board)

    # perform BFS algorithm
    start = time.time()
    output = bfs.solve()
    end = time.time()

    print(f'time: {(end - start) * 1000} ms')
    print('path_to_goal:',output['path_to_goal'])
    print('cost_of_path:',output['cost_of_path'])
    print('nodes_expanded:',output['nodes_expanded'])
    print('search_depth:',output['search_depth'])
    print('path:\n', output['goal_steps'])

if __name__ == '__main__':
    main()
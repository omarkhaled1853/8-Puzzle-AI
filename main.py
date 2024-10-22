import sys
from bfs import BFS

def print_path(path):
    # printing path for reaching the goal
    print(f'Path to the goal:')
    for arr in path:
        for r in arr:
            print(r)
        print('*'*100)

def print_expanded_nodes(expanded):
    # printing number of visited nodes and the visited nodes itself 
    print(f'Number of expanded nodes: {len(expanded)}')
    print(f'Expanded nodes:')
    for node in expanded:
        print(node.get_empty_tile_location())
        for r in node.get_board():
            print(r)
        print('*'*50)

def print_forntier_nodes(frontier):
    # printing number of in progressed nodes but not visited and the progressed nodes itself 
    print(f'Number of not expanded nodes: {len(frontier)}')
    print(f'Not expanded nodes:')
    for node in frontier:
        print(node.get_empty_tile_location())
        for r in node.get_board():
            print(r)
        print('*'*50)


def main():
    # example
    board = [
        [1, 2, 5],
        [3, 4, 0],
        [6, 7, 8]
    ]

    bfs = BFS(board)

    # perform BFS algorithm
    movements, cost, number_of_expanded_nodes, max_depth_search, path = bfs.solve()

    print(movements, cost, number_of_expanded_nodes, max_depth_search)
    print_path(path)
    # print("="*100)

    # print_expanded_nodes(expanded)
    # print("="*100)

if __name__ == '__main__':
    main()
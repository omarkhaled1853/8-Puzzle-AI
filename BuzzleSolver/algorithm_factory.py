from BuzzleSolver.search import *
from BuzzleSolver.BFS.bfs import *
from BuzzleSolver.DFS.dfs import *
from BuzzleSolver.A_star.a_star import *
from BuzzleSolver.A_star.heuristic_factory import *

# factory class to returun specific search alogrithm
class Algorithm_Factory:
    @staticmethod
    def get_technique(algorithm_name: str, intial_state: int, limit = None, heuristic = None) -> Search:
        if algorithm_name == 'BFS':
            return BFS(intial_state)
        elif algorithm_name == 'DFS':
            return DFS(intial_state)
        elif algorithm_name == 'IDFS':
            return DFS(intial_state, limit)
        elif algorithm_name == 'A*':
            heu = Heuristic_Factory.get_heuristic(heuristic)
            return A_star(intial_state, heu)
        else: None
# factory class to returun specific search alogrithm
class Factory:
    def get_technique(algorithm_name: str, intial_state: int, limit = None, heuristic = None):
        if algorithm_name == 'BFS':
            return BFS(intial_state)
        elif algorithm_name == 'DFS':
            return DFS(intial_state)
        elif algorithm_name == 'IDFS':
            return IDFS(intial_state, limit)
        elif algorithm_name == 'A_star':
            return A_Star(intial_state, heuristic)
        else: None
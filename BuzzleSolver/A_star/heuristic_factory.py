from BuzzleSolver.A_star.heuristic import *

class Heuristic_Factory:
    @staticmethod
    def get_heuristic(heuristic):
        heu = Heuristics()
        if heuristic == 'Manhattan':
            return heu.Manhattan_Distance
        elif heuristic == 'Euclidean':
            return heu.Euclidean_Distance
        else:
            return None
            
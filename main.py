from Heuristics import Heuristics
from A_Star import A_Star


heu = Heuristics()
astar = A_Star(board=142658730, heuristic=heu.Euclidean_Distance)
res = astar.solve()


print(res['path_to_goal'])
print(res['cost_of_path'])
print(res['nodes_expanded'])
print(res['search_depth'])
print(res['goal_steps'''])

import numpy as np
from greedy import GreedyTSP

# graph as the adjacency matrix
graph1 = np.array([[0, 30, 19, 10, 7],
                  [8, 0, 9, 15, 18],
                  [29, 13, 0, 5, 12],
                  [3, 11, 6, 0, 3],
                  [1, 4, 30, 4, 0]])

greedy = GreedyTSP(graph=graph1, num_cities=graph1.shape[0])
greedy.find_shortest_path(city=0)
print(greedy.get_total_cost())
print(greedy.get_shortest_path())

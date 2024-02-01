from itertools import permutations


class BruteForceTSP():
    def __init__(self, graph, num_cities):
        self.graph = graph
        self.num_vertices = num_cities
        self.total_cost = 0
        self.path = None
    
    def find_path(self):
        vertices = list(range(self.num_vertices))
        min_cost = float('inf')
        all_path = permutations(vertices)
        
        for path in all_path:
            cost = self.calculate_cost(path)
            if cost < min_cost:
                min_cost = cost
                self.path = path
        
    def calculate_cost(self, path):
        total_cost = 0
        for i in range(len(path) - 1):
            total_cost += self.graph[path[i]][path[i + 1]]
        total_cost += self.graph[path[-1]][path[0]]
        return total_cost
    
    def get_shortest_path(self):
        return self.path

    def get_total_cost(self):
        return self.total_cost

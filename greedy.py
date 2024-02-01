import numpy as np 


class GreedyTSP():
    
    def __init__(self, graph, num_cities):
        self.graph = graph
        self.num_cities = num_cities
        self.total_cost = 0
        self.path = []
        self.visited_cities = np.zeros(num_cities, dtype=int)

    def find_shortest_path(self, city):
        nearest_city = self.num_cities
        min_duration = float('inf')
        self.visited_cities[city] = 1
        self.path.append(city)

        for k in range(self.num_cities):
            if (self.graph[city][k] != 0) and (self.visited_cities[k] == 0):
                if self.graph[city][k] < min_duration:
                    min_duration = self.graph[city][k]
                    nearest_city = k
            
        if min_duration != float('inf'):
            self.total_cost = self.total_cost + min_duration

        if nearest_city == self.num_cities:
            nearest_city = 0
            self.path.append(nearest_city)
            self.total_cost = self.total_cost + self.graph[city][nearest_city] 
            return 
            
        self.find_shortest_path(nearest_city)

    def get_shortest_path(self):
        return self.path

    def get_total_cost(self):
        return self.total_cost

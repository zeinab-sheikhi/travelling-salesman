from itertools import permutations


def calculate_total_distance(tour, distances):
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += distances[tour[i]][tour[i + 1]]
    total_distance += distances[tour[-1]][tour[0]]
    return total_distance


def brute_force_tsp(distances):
    num_cities = len(distances)
    cities = list(range(num_cities))
    all_tours = permutations(cities)

    min_dist = float('inf')
    optimal_tour = None

    for tour in all_tours:
        total_distance = calculate_total_distance(tour, distances)
        if total_distance < min_dist:
            min_dist = total_distance
            optimal_tour = tour
    return {"path": optimal_tour, "cost": min_dist}

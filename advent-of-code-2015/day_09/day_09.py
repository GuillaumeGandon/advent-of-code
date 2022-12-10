from itertools import permutations


def split_row(row):
    tmp = row.split()
    return (tmp[0], tmp[2]), int(tmp[4])


def compute_distance(route):
    distance = 0
    for i in range(len(route) - 1):
        distance += location_pairs[(route[i], route[i + 1])]
    return distance


location_pairs = dict(split_row(row) for row in open('input').read().splitlines())
location_pairs.update({k[::-1]: v for k, v in location_pairs.items()})
cities = set(city for city_pair in location_pairs for city in city_pair)
possible_routes = tuple(permutations(cities))

print(f"Answer part one: {min(compute_distance(route) for route in possible_routes)}")
print(f"Answer part two: {max(compute_distance(route) for route in possible_routes)}")

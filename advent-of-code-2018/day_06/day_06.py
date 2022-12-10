from collections import Counter
from itertools import takewhile

points = tuple(tuple(map(int, row.split(", "))) for row in open("input").read().splitlines())

min_x = min(x for x, y in points)
max_x = max(x for x, y in points)
min_y = min(y for x, y in points)
max_y = max(y for x, y in points)


def compute_manhattan_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def find_closest_point(x, y):
    distances = sorted((compute_manhattan_distance((x, y), p), p) for p in points)
    closest = [*takewhile(lambda t: t[0] == distances[0][0], distances)]
    if len(closest) > 1:
        return None
    return closest[0][1]


def sum_manhattan_distances(x, y):
    return sum(compute_manhattan_distance((x, y), point) for point in points)


grid = tuple(tuple(find_closest_point(x, y) for x in range(min_x, max_x + 1)) for y in range(min_y, max_y + 1))

edges = set(
    grid[y][x]
    for x in range(0, len(grid[0]))
    for y in range(0, len(grid))
    if x in {0, len(grid[0]) - 1} or y in {0, len(grid) - 1}
)

finite_area = Counter(point for row in grid for point in row if point not in edges)

print(f"Answer part one: {max(finite_area.values())}")

part_2 = sum(
    1 for x in range(min_x, max_x + 1) for y in range(min_y, max_y + 1) if sum_manhattan_distances(x, y) < 10000
)
print(f"Answer part two: {part_2}")

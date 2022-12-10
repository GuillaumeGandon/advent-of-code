from collections import defaultdict
from itertools import product


def inclusive_range(start, stop):
    step = 1 if stop >= start else -1
    return range(start, stop + step, step)


def compute(part_two=False):
    dangerous_areas = defaultdict(lambda: 0)  # type: dict[tuple, int]
    for (x1, y1), (x2, y2) in lines:
        if x1 == x2 or y1 == y2:
            for x, y in product(inclusive_range(x1, x2), inclusive_range(y1, y2)):
                dangerous_areas[(x, y)] += 1
        elif part_two:
            for x, y in zip(inclusive_range(x1, x2), inclusive_range(y1, y2)):
                dangerous_areas[(x, y)] += 1
    return sum(1 for _k, v in dangerous_areas.items() if v >= 2)


lines = tuple(
    tuple(tuple(map(int, x.split(","))) for x in line.split(" -> ")) for line in open("input").read().splitlines()
)


print(f"Answer part one: {compute()}")
print(f"Answer part two: {compute(part_two=True)}")

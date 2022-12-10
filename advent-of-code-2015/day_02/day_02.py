from math import prod
from itertools import combinations


def paper_surface(dim):
    areas = tuple(map(prod, combinations(dim, 2)))
    smallest_area = min(areas)
    return sum(area * 2 for area in areas) + smallest_area


def ribbon_length(dim):
    return sum(min(tuple(combinations(dim, 2)), key=sum)) * 2 + prod(dim)


dims = tuple(tuple(map(int, row.split('x'))) for row in open('input').read().splitlines())
print(f'Answer part one: {sum(paper_surface(dim) for dim in dims)}')
print(f'Answer part two: {sum(ribbon_length(dim) for dim in dims)}')

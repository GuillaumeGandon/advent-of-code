from math import prod
from itertools import combinations

weights = tuple(map(int, open('input').read().splitlines()))


def solve(nb_group):
    targeted_weight = sum(weights) // nb_group
    i = 0
    valid_combinations = None
    while not valid_combinations:
        i += 1
        valid_combinations = tuple(
            comb
            for comb in combinations(weights, i)
            if sum(comb) == targeted_weight
        )

    return min(map(prod, valid_combinations))


print(f"Answer part one: {solve(nb_group=3)}")
print(f"Answer part two: {solve(nb_group=4)}")

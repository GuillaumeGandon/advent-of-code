from functools import cache
from statistics import median


@cache
def sum_of_n_first_integers(n):
    return n * (n + 1) // 2


crabs = tuple(map(int, open("input").read().split(",")))

print(f"Answer part one: {sum(abs(pos - (align_position := int(median(crabs)))) for pos in crabs)}")

part_two = min(sum(sum_of_n_first_integers(abs(pos - i)) for pos in crabs) for i in range(min(crabs), max(crabs) + 1))
print(f"Answer part two: {part_two}")

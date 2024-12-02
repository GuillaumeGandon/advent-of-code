from itertools import combinations


def is_safe(l):
    return (all(l[i] < l[i + 1] for i in range(len(l) - 1)) or all(l[i] > l[i + 1] for i in range(len(l) - 1))) and all(
        1 <= abs(l[i] - l[i + 1]) <= 3 for i in range(len(l) - 1)
    )


def is_safe_part_two(l):
    return any(is_safe(c) for c in combinations(l, len(l) - 1))


reports = [list(map(int, line.split())) for line in open("input").read().splitlines()]

print(f"Answer part one: {sum(is_safe(levels) for levels in reports)}")
print(f"Answer part two: {sum(is_safe_part_two(levels) for levels in reports)}")

from collections import defaultdict
from functools import cmp_to_key


def compare(item1, item2):
    if item2 in rules[item1]:
        return -1
    elif item1 in rules[item2]:
        return 1
    else:
        return 0


a, b = open("input").read().split("\n\n")

rules = defaultdict(set)
for k, v in (tuple(map(int, line.split("|"))) for line in a.splitlines()):
    rules[k].add(v)

updates = [list(map(int, line.split(","))) for line in b.splitlines()]

print(f"Answer part one: {sum(u[len(u) // 2] for u in updates if u == sorted(u, key=cmp_to_key(compare)))}")
print(f"Answer part two: {sum(us[len(us) // 2] for u in updates if u != (us := sorted(u, key=cmp_to_key(compare))))}")

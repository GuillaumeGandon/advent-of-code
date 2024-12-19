from collections import defaultdict


def is_possible(design):
    if design in seen_designs:
        return seen_designs[design]

    if not design:
        seen_designs[design] = 1
        return 1

    nb_different_ways = 0
    for p in patterns_dict[design[0]]:
        if design.startswith(p):
            nb_different_ways += is_possible(design[len(p) :])
    seen_designs[design] = nb_different_ways
    return nb_different_ways


patterns, designs = open("input").read().split("\n\n")
patterns_dict = defaultdict(set)
for p in patterns.split(", "):
    patterns_dict[p[0]].add(p)

seen_designs = {}

print(f"Answer part one: {sum(is_possible(d) != 0 for d in designs.splitlines())}")
print(f"Answer part two: {sum(is_possible(d) for d in designs.splitlines())}")

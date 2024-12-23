from collections import defaultdict
from itertools import combinations


connections = defaultdict(set)
for line in open("input").read().splitlines():
    a, b = line.split("-")
    connections[a].add(b)
    connections[b].add(a)

three_connections_with_t = set()
for k, v in connections.items():
    if k.startswith("t"):
        for c in combinations(v, 2):
            for x in c:
                if all(all(y in connections[x] for y in set(c) - set([x])) for x in c):
                    three_connections_with_t.add(tuple(sorted(tuple([k]) + c)))


largest_set_of_computers = tuple()
for k, v in connections.items():
    for i in reversed(range(len(v))):
        if i + 1 > len(largest_set_of_computers):
            for c in combinations(v, i):
                for x in c:
                    if all(all(y in connections[x] for y in set(c) - set([x])) for x in c):
                        largest_set_of_computers = tuple(sorted(tuple([k]) + c))


print(f"Answer part one: {len(three_connections_with_t)}")
print(f"Answer part two: {",".join(largest_set_of_computers)}")

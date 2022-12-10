from collections import defaultdict


def find_paths(cave="start", path=("start",), disable_second_visit=True):
    if cave == "end":
        paths.add(path)
        return

    for connected_cave in connections[cave]:
        d_s_v = disable_second_visit
        if connected_cave.islower() and connected_cave in path:
            if disable_second_visit:
                continue
            d_s_v = True
        find_paths(connected_cave, path + (connected_cave,), d_s_v)


connections = defaultdict(set)

for a, b in (tuple(line.split("-")) for line in open("input").read().splitlines()):
    if b != "start" and a != "end":
        connections[a].add(b)
    if a != "start" and b != "end":
        connections[b].add(a)

paths = set()
find_paths()
print(f"Answer part one: {len(paths)}")

paths = set()
find_paths(disable_second_visit=False)
print(f"Answer part two: {len(paths)}")

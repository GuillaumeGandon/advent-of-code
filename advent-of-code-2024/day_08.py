from collections import defaultdict
from itertools import combinations

data = open("input").read().splitlines()

R = len(data)
C = len(data[0])


antennas = {(x, y): data[y][x] for y in range(R) for x in range(C) if data[y][x] != "."}

antennas_by_frequency = defaultdict(list)

for k, v in antennas.items():
    antennas_by_frequency[v].append(k)

antinodes = set()
for k, v in antennas_by_frequency.items():
    for (x1, y1), (x2, y2) in combinations(v, 2):
        xx = x1 - x2
        yy = y1 - y2

        if 0 <= x1 + xx < C and 0 <= y1 + yy < R:
            antinodes.add((x1 + xx, y1 + yy))
        if 0 <= x2 - xx < C and 0 <= y2 - yy < R:
            antinodes.add((x2 - xx, y2 - yy))


print(f"Answer part one: {len(antinodes)}")

antinodes = set()
for k, v in antennas_by_frequency.items():
    for (x1, y1), (x2, y2) in combinations(v, 2):
        xx = x1
        yy = y1

        dx = x1 - x2
        dy = y1 - y2

        while 0 <= xx < C and 0 <= yy < R:
            antinodes.add((xx, yy))
            xx += dx
            yy += dy

        xx = x2
        yy = y2
        while 0 <= xx < C and 0 <= yy < R:
            antinodes.add((xx, yy))
            xx -= dx
            yy -= dy


print(f"Answer part two: {len(antinodes)}")

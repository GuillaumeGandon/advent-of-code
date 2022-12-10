from collections import defaultdict
from itertools import product

squares = {
    (splitted_row := row.split())[0].replace("#", ""): (
        tuple(map(int, splitted_row[2].replace(":", "").split(","))),
        tuple(map(int, splitted_row[3].split("x"))),
    )
    for row in open("input").read().splitlines()
}

grid = defaultdict(lambda: 0)

for id, ((x, y), (w, h)) in squares.items():
    for xx, yy in product(range(x, x + w), range(y, y + h)):
        grid[(xx, yy)] += 1

claim_without_overlap = None
for id, ((x, y), (w, h)) in squares.items():
    if all(grid[(xx, yy)] == 1 for xx, yy in product(range(x, x + w), range(y, y + h))):
        claim_without_overlap = id


print(f"Answer part one: {sum(1 for pos in grid if grid[pos]>=2)}")
print(f"Answer part two: {claim_without_overlap}")

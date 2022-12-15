from shapely.geometry.polygon import Polygon

data = tuple(
    tuple(
        tuple(int(y.replace("Sensor at x=", "").replace("x=", "").replace("y=", "")) for y in x.split(", "))
        for x in row.split(": closest beacon is at ")
    )
    for row in open("input").read().splitlines()
)


grid = {p: "S" if i == 0 else "B" for row in data for i, p in enumerate(row)}


def solve_part_1(y):
    res = 0
    for ((x1, y1), (x2, y2)) in data:
        man_dist = abs(x1 - x2) + abs(y1 - y2)
        abs_y = abs(y1 - y)
        x_min = x1 - (man_dist - abs_y)
        x_max = x1 + (man_dist - abs_y) + 1
        for x in range(x_min, x_max):
            if (x, y) not in grid:
                grid[(x, y)] = "#"
                res += 1
    return res


def solve_part_2(max_cord):
    polygons = (
        Polygon(
            [
                (x1 - (man_dist := abs(x1 - x2) + abs(y1 - y2)) - 0.5, y1),
                (x1, y1 - man_dist - 0.5),
                (x1 + man_dist + 0.5, y1),
                (x1, y1 + man_dist + 0.5),
            ]
        )
        for ((x1, y1), (x2, y2)) in data
    )

    mask = Polygon()
    for p in polygons:
        mask = mask.union(p)

    frame = Polygon([(0, 0), (max_cord, 0), (max_cord, max_cord), (0, max_cord)])

    diff = frame.difference(mask)
    x, y = tuple(diff.centroid.coords)[0]
    return int(x * max_cord + y)


print(f"Answer part one: {solve_part_1(y=2000000)}")
print(f"Answer part two: {solve_part_2(max_cord=4000000)}")

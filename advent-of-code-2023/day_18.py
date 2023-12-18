def find_area(points):
    n = len(points)
    return (
        abs(sum(points[i][0] * points[(i + 1) % n][1] - points[(i + 1) % n][0] * points[i][1] for i in range(n))) // 2
    )


def solve(part_2=False):
    x, y = 0, 0
    lagoon_edge = []
    perimeter = 0
    for a, b, c in (line.split() for line in open("input").read().splitlines()):
        n = int(b)
        if part_2:
            n = int("0x" + c[2:-2], 0)
            a = int(c[-2])
        perimeter += n
        if a == "R" or a == 0:
            x += n
        elif a == "D" or a == 1:
            y += n
        elif a == "L" or a == 2:
            x -= n
        else:
            y -= n
        lagoon_edge.append((x, y))

    return perimeter // 2 + find_area(lagoon_edge) + 1


print(f"Answer part one: {solve()}")
print(f"Answer part two: {solve(part_2=True)}")

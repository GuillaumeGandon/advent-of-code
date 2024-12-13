def solve(part_2=False):
    res = 0
    for block in (block.splitlines() for block in open("input").read().split("\n\n")):
        ax, ay = list(map(int, block[0].split(": ")[-1].replace("X+", "").split(", Y+")))
        bx, by = list(map(int, block[1].split(": ")[-1].replace("X+", "").split(", Y+")))
        px, py = list(map(int, block[2].split(": ")[-1].replace("X=", "").split(", Y=")))
        if part_2:
            px += 10000000000000
            py += 10000000000000
        nb_b = round((py - ay * px / ax) / (by - ay * bx / ax))
        nb_a = round((px - nb_b * bx) / ax)
        if nb_a * ax + nb_b * bx == px and nb_a * ay + nb_b * by == py:
            res += 3 * nb_a + nb_b
    return res


print(f"Answer part one: {solve()}")
print(f"Answer part two: {solve(part_2=True)}")

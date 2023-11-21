from copy import deepcopy
from itertools import combinations

cubes = tuple(tuple(map(int, row.split(","))) for row in open("input").read().splitlines())


def touch(c1, c2):
    x1, y1, z1 = c1
    x2, y2, z2 = c2
    return (
        (x1 == x2 and y1 == y2 and (z1 == z2 + 1 or z1 + 1 == z2))
        or (x1 == x2 and z1 == z2 and (y1 == y2 + 1 or y1 + 1 == y2))
        or (y1 == y2 and z1 == z2 and (x1 == x2 + 1 or x1 + 1 == x2))
    )


def count_touch(c1, droplet):
    return 6 - sum(1 for c2 in droplet if touch(c1, c2))


def compute_droplets(cubes):
    droplets = []
    processed_cube = set()
    for c1 in cubes:
        if c1 not in processed_cube:
            droplet = set((c1,))
            add_cube = True
            while add_cube:
                add_cube = False
                for c2 in cubes:
                    if c2 not in droplet and any(touch(c2, c) for c in droplet):
                        droplet.add(c2)
                        add_cube = True

            droplets.append(droplet)
            processed_cube.update(droplet)

    return droplets


droplets = compute_droplets(cubes)
part_one = sum(count_touch(c, d) for d in droplets for c in d)
print(f"Answer part one: {part_one}")


x_min = min(cubes, key=lambda x: x[0])[0]
x_max = max(cubes, key=lambda x: x[0])[0]
y_min = min(cubes, key=lambda x: x[1])[1]
y_max = max(cubes, key=lambda x: x[1])[1]
z_min = min(cubes, key=lambda x: x[2])[2]
z_max = max(cubes, key=lambda x: x[2])[2]

exterior_cubes = tuple(
    (x, y, z)
    for x in range(x_min, x_max + 1)
    for y in range(y_min, y_max + 1)
    for z in range(z_min, z_max + 1)
    if not any((x, y, z) in d for d in droplets)
)
exterior_droplets = compute_droplets(exterior_cubes)
cleaned = tuple(
    d
    for d in exterior_droplets
    if x_min != min(d, key=lambda x: x[0])[0]
    and x_max != max(d, key=lambda x: x[0])[0]
    and y_min != min(d, key=lambda x: x[1])[1]
    and y_max != max(d, key=lambda x: x[1])[1]
    and z_min != min(d, key=lambda x: x[2])[2]
    and z_max != max(d, key=lambda x: x[2])[2]
)


print(f"Answer part two: {part_one - sum(count_touch(c, d) for d in cleaned for c in d)}")

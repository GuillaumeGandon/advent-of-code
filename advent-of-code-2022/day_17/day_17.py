jets = open("input").read().strip()

WIDE = 7


shapes = (
    (0, 1, 2, 3),
    (1j, 1, 1 + 1j, 1 + 2j, 2 + 1j),
    (0, 1, 2, 2 + 1j, 2 + 2j),
    (0, 1j, 2j, 3j),
    (0, 1, 1j, 1 + 1j),
)


def move_shape(r, m):
    return tuple(p + m for p in r)


def jet_direction(jet):
    return 1 if jet == ">" else -1


def print_rocks(stopped_rocks):
    x_min = 0
    x_max = WIDE
    y_min = 0
    y_max = int(max(r.imag for r in stopped_rocks))
    for y in range(y_max, y_min, -1):
        line = ""
        for x in range(x_min - 1, x_max + 1):
            if x == -1 or x == WIDE:
                line += "|"
            elif (x + y * 1j) in stopped_rocks:
                line += "#"
            else:
                line += "."
        print(line)
    print("+-------+")


def add_shape_to_stopped_rocks(shape, stopped_rocks, i):
    check_lines = sorted(set(int(s.imag) for s in shape), reverse=True)
    stopped_rocks.update(set(shape))
    for y in check_lines:
        if all(x + y * 1j in stopped_rocks for x in range(0, WIDE)):
            if y == max(r.imag for r in stopped_rocks):
                print(i, max(r.imag for r in stopped_rocks))
            return set(r for r in stopped_rocks if r.imag >= y)
    return stopped_rocks


def solve(nb_rocks):
    jet_idx = 0
    stopped_rocks = set(i for i in range(WIDE))
    for i in range(nb_rocks):
        initial = 2 + max(r.imag for r in stopped_rocks) * 1j + 4j
        shape = move_shape(shapes[i % 5], initial)
        while 1:
            next_shape = move_shape(shape, jet_direction(jets[jet_idx % len(jets)]))
            jet_idx += 1
            if not any(r in stopped_rocks for r in next_shape):
                if 0 <= next_shape[0].real and next_shape[-1].real < WIDE:
                    shape = next_shape

            next_shape = move_shape(shape, -1j)
            if not any(r in stopped_rocks for r in next_shape):
                shape = next_shape
            else:
                stopped_rocks = add_shape_to_stopped_rocks(shape, stopped_rocks, i)
                break

    # print_rocks(stopped_rocks)

    return max(r.imag for r in stopped_rocks)


print(f"Answer part one: {solve(nb_rocks=2022)}")


def part_two(nb_rocks):
    return int((nb_rocks - 650) // 1735 * 2673 + solve(nb_rocks=(nb_rocks - 650) % 1735 + 650))


print(f"Answer part two: {part_two(1000000000000)}")

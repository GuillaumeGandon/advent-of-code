input = 361527

adjacents = (
    (-1 + 1j),
    (0 + 1j),
    (1 + 1j),
    (-1 + 0j),
    (1 + 0j),
    (-1 - 1j),
    (0 - 1j),
    (1 - 1j),
)


def manhattan_distance(pos):
    return int(abs(pos.real) + abs(pos.imag))


def sum_all_agjacent_squares(grid, pos):
    return sum(grid[pos + adj] for adj in adjacents if pos + adj in grid)


def build_grid():
    grid = {1: (0 + 0j)}

    step = 1
    move = 1 + 0j
    pos = 0 + 0j
    value = 1
    while input not in grid:
        for _ in range(2):
            for _ in range(step):
                pos += move
                value += 1
                grid[value] = pos
            move *= 0 + 1j
        step += 1

    return grid


def build_grid_v2():
    grid = {(0 + 0j): 1}
    move = 1 + 0j
    pos = 0 + 0j
    value = 1
    while input > value:
        pos += move
        value = sum_all_agjacent_squares(grid, pos)
        grid[pos] = value
        if pos + move * (0 + 1j) not in grid:
            move *= 0 + 1j
    return value


grid = build_grid()

print(grid[input], manhattan_distance(grid[input]))
print(build_grid_v2())

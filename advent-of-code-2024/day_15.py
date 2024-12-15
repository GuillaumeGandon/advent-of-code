DIRECTIONS = {"<": -1, "v": 1j, ">": 1, "^": -1j}
WIDENING = {"#": "##", "O": "[]", ".": "..", "@": "@."}


def can_move(robot, m, wall, boxes):
    positions, seen = [robot], []
    while 1:
        tmp = []
        for p in positions:
            seen.append(p)
            next_pos = p + m
            if next_pos in wall:
                return {}
            elif next_pos in boxes:
                tmp.append(next_pos)
                if m.real == 0 and boxes[next_pos] == "[":
                    tmp.append(next_pos + 1)
                elif m.real == 0 and boxes[next_pos] == "]":
                    tmp.append(next_pos - 1)
        if not tmp:
            return seen
        positions = tmp


def solve(part_2=False):
    warehouse_map, moves = [block.splitlines() for block in open("input").read().split("\n\n")]
    if part_2:
        warehouse_map = ["".join(WIDENING[c] for c in line) for line in warehouse_map]
    grid = {x + y * 1j: c for y, line in enumerate(warehouse_map) for x, c in enumerate(line) if c != "."}

    robot = [k for k, v in grid.items() if v == "@"][0]
    wall = {k for k, v in grid.items() if v == "#"}

    for m in (DIRECTIONS[c] for line in moves for c in line):
        boxes = {k: v for k, v in grid.items() if v in "O[]"}
        to_move = can_move(robot, m, wall, boxes)
        if to_move:
            robot = to_move[0] + m
            for p in to_move[::-1]:
                if p in grid:
                    grid[p + m] = grid[p]
                    del grid[p]
    return int(sum(k.real + k.imag * 100 for k, v in grid.items() if v in "O["))


print(f"Answer part one: {solve()}")
print(f"Answer part two: {solve(part_2=True)}")

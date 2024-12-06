from collections import defaultdict


def find_start_position():
    for k, v in map.items():
        if v == "^":
            return k


def find_guard_moves(obstruction=None):
    guard = start_position
    direction = -1j
    visit_positions = defaultdict(set)
    visit_positions[guard].add(direction)

    while 1:
        next_position = guard + direction
        if next_position not in map:
            return visit_positions
        elif next_position in visit_positions and direction in visit_positions[next_position]:
            return None

        if map[next_position] == "#" or next_position == obstruction:
            direction *= 1j
        else:
            guard = next_position
            visit_positions[guard].add(direction)


map = {(x + y * 1j): v for y, line in enumerate(open("input").read().splitlines()) for x, v in enumerate(line)}

start_position = find_start_position()
visited_positions = find_guard_moves()
print(f"Answer part one: {len(visited_positions)}")

obstructions = set()
for vp, directions in visited_positions.items():
    for d in directions.union(set((0,))):
        next_position = vp + d
        if (
            next_position in map
            and map[next_position] != "#"
            and next_position not in obstructions
            and next_position != start_position
        ):
            if find_guard_moves(obstruction=next_position) is None:
                obstructions.add(next_position)

print(f"Answer part two: {(len(obstructions))}")

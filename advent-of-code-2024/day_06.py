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
for vp in visited_positions:
    if vp not in obstructions and vp != start_position and find_guard_moves(obstruction=vp) is None:
        obstructions.add(vp)

print(f"Answer part two: {(len(obstructions))}")

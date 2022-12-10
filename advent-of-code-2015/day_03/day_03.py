MOVES = {
    '^': 0 + 1j,
    'v': 0 - 1j,
    '<': -1 + 0j,
    '>': +1 + 0j
}


def deliver_house(directions):
    pos = 0 + 0j
    all_pos = [pos]
    for d in directions:
        pos += MOVES[d]
        all_pos.append(pos)
    return all_pos


directions = open('input').read()
print(f"Answer part one: {len(set(deliver_house(directions)))}")
print(f"Answer part two: {len(set(deliver_house(directions[::2]) + deliver_house(directions[1::2])))}")

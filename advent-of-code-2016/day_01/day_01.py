TURNS = {"R": -1j, "L": 1j}
instructions = tuple((inst[0], int(inst[1:])) for inst in open("input").read().strip().split(", "))

position, direction = (0 + 0j), (0 + 1j)
visited_locations = set()
first_twice_location = 0 + 0j
for turn, dist in instructions:
    direction *= TURNS[turn]
    for _ in range(dist):
        visited_locations.add(position)
        position += direction
        if not first_twice_location and position in visited_locations:
            first_twice_location = position

print(f"Answer part one: {int(abs(position.real) + abs(position.imag))}")
print(f"Answer part two: {int(abs(first_twice_location.real) + abs(first_twice_location.imag))}")

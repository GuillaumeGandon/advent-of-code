direction = {
    'R': 1 + 0j,
    'L': -1 + 0j,
    'D': 0 + 1j,
    'U': 0 - 1j
}


def compute_points(wire):
    pos = (0 + 0j)
    dist = 0
    res = {}
    for path in wire:
        for i in range(int(path[1:])):
            dist += 1
            pos += direction[path[0]]
            if pos not in res or pos in res and dist < res[pos]:
                res[pos] = dist
    return res


wires = tuple(
    tuple(wire.split(','))
    for wire in open('input').read().splitlines()
)
points = [compute_points(wire) for wire in wires]
intersections = set.intersection(*[set(p.keys()) for p in points])

man_point = min(intersections, key=abs)
print(f'Answer part one: {int(abs(man_point.real) + abs(man_point.imag))}')

min_dist = min(sum(p[pos] for p in points) for pos in intersections)
print(f'Answer part two: {min_dist}')

orbits = dict(
    reversed(wire.split(')'))
    for wire in open('input').read().splitlines()
)


def get_orbited(o):
    if o in orbits:
        return (o,) + get_orbited(orbits[o])
    return tuple()


print(f'Answer part one: {sum(len(get_orbited(obj)) for obj in orbits)}')

diff = set.symmetric_difference(set(get_orbited('YOU')), set(get_orbited('SAN')))
diff.remove('YOU')
diff.remove('SAN')
print(f'Answer part two: {len(diff)}')

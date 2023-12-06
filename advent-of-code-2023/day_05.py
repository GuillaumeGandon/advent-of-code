lines = tuple(block.splitlines() for block in open("input").read().split("\n\n"))
seeds = tuple(map(int, lines[0][0].split(": ")[1].split()))
maps = {line[0][:-1]: tuple(tuple(map(int, x.split())) for x in line[1:]) for line in lines[1:]}


def find_next_location(k, location):
    m = maps[k]
    for a, b, c in m:
        if b <= location < b + c:
            return a + location - b
    return location


def find_last_location(k, location):
    for a, b, c in maps[k]:
        if a <= location < a + c:
            return b + location - a
    return location


part_1 = float("inf")
for seed in seeds:
    location = seed
    for k in maps:
        location = find_next_location(k, location)
    part_1 = min(part_1, location)

print(f"Answer part one: {part_1}")

reversed_maps = tuple(reversed(maps))
seeds_zipped = tuple(zip(seeds[0::2], seeds[1::2]))
i = 0
while 1:
    if i % 1000000 == 0:
        print(i)
    location = i
    for k in reversed_maps:
        location = find_last_location(k, location)
    if any(s <= location < s + r for s, r in seeds_zipped):
        break
    i += 1


print(f"Answer part two: {i}")

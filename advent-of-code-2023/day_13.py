patterns = tuple(pattern.splitlines() for pattern in open("input").read().split("\n\n"))


def find_horizontal_reflection(pattern, part_2=False):
    width = len(pattern[0])
    for x in range(1, width):
        if x <= width / 2:
            a = tuple(pattern[y][:x] for y in range(len(pattern)))
        else:
            a = tuple(pattern[y][x - (width - x) : x] for y in range(len(pattern)))
        b = tuple(pattern[y][x : x + x][::-1] for y in range(len(pattern)))

        if part_2:
            if sum(aa != bb for i in range(len(a)) for aa, bb in zip(a[i], b[i])) == 1:
                return x
        else:
            if a == b:
                return x
    return None


def find_vertical_reflection(pattern, part_2):
    transpose_pattern = tuple(map(tuple, zip(*pattern)))
    return find_horizontal_reflection(transpose_pattern, part_2)


def find_reflection(pattern, part_2=False):
    if horizontal_reflection := find_horizontal_reflection(pattern, part_2):
        return horizontal_reflection

    if vertical_reflection := find_vertical_reflection(pattern, part_2):
        return vertical_reflection * 100


part_1 = sum(find_reflection(pattern) for pattern in patterns)
part_2 = sum(find_reflection(pattern, part_2=True) for pattern in patterns)

print(f"Answer part one: {part_1}")
print(f"Answer part two: {part_2}")

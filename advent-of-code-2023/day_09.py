def find_next_value(line, part_2=False):
    direction = -1
    if part_2:
        direction = 0
    values = [line[direction]]
    while any(nb != 0 for nb in line):
        line = [line[i + 1] - line[i] for i in range(len(line) - 1)]
        values.append(line[direction])

    if part_2:
        res = 0
        for v in reversed(values):
            res = v - res
        return res

    return sum(values)


lines = tuple(tuple(map(int, line.split())) for line in open("input").read().splitlines())


part_1 = sum(find_next_value(line) for line in lines)
part_2 = sum(find_next_value(line, part_2=True) for line in lines)


print(f"Answer part one: {part_1}")
print(f"Answer part two: {part_2}")

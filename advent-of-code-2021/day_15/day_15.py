def compute(part_two=False):
    risk_levels = tuple(tuple(map(int, line)) for line in open("input").read().splitlines())
    if part_two:
        risk_levels_2 = tuple(
            tuple(v + i if v + i < 10 else (v + i) % 9 for i in range(5) for v in risk_levels[y])
            for y in range(len(risk_levels))
        )
        risk_levels_2 = tuple(
            tuple(v + i if v + i < 10 else (v + i) % 9 for v in risk_levels_2[y])
            for i in range(5)
            for y in range(len(risk_levels_2))
        )
        risk_levels = risk_levels_2
    max_x, max_y = len(risk_levels[0]) - 1, len(risk_levels) - 1

    risk_map = {
        (x, y): sum(risk_levels[0][0 : x + 1]) + sum(row[x] for row in risk_levels[0 : y + 1])
        for y in range(max_y + 1)
        for x in range(max_x + 1)
    }
    risk_map[(0, 0)] = 0

    improvement = True
    while improvement:
        improvement = False

        for y in range(max_y + 1):
            for x in range(max_x + 1):
                risk = risk_levels[y][x]

                if y + 1 <= max_y and risk_map[(x, y + 1)] + risk < risk_map[(x, y)]:
                    improvement = True
                    risk_map[(x, y)] = risk_map[(x, y + 1)] + risk
                if x + 1 <= max_x and risk_map[(x + 1, y)] + risk < risk_map[(x, y)]:
                    improvement = True
                    risk_map[(x, y)] = risk_map[(x + 1, y)] + risk
                if y - 1 >= 0 and risk_map[(x, y - 1)] + risk < risk_map[(x, y)]:
                    improvement = True
                    risk_map[(x, y)] = risk_map[(x, y - 1)] + risk
                if x - 1 >= 0 and risk_map[(x - 1, y)] + risk < risk_map[(x, y)]:
                    improvement = True
                    risk_map[(x, y)] = risk_map[(x - 1, y)] + risk

    return risk_map[(max_x, max_y)]


print(f"Answer part one: {compute()}")
print(f"Answer part two: {compute(part_two=True)}")

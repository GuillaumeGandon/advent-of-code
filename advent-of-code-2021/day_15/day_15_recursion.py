import sys

sys.setrecursionlimit(10000)

data = tuple(tuple(map(int, line)) for line in open("input").read().splitlines())

data2 = tuple(tuple(v + i if v + i < 10 else (v + i) % 9 for i in range(5) for v in data[y]) for y in range(len(data)))
data2 = tuple(
    tuple(v + i if v + i < 10 else (v + i) % 9 for v in data2[y]) for i in range(5) for y in range(len(data2))
)
# data = data2
max_x, max_y = len(data[0]) - 1, len(data) - 1
print(max_x, max_y)


risk_map = {
    (x, y): sum(data[0][0 : x + 1]) + sum(row[x] for row in data[0 : y + 1])
    for y in range(max_y + 1)
    for x in range(max_x + 1)
}


def compute(current_risk, x, y):
    if current_risk >= risk_map[(x, y)]:
        return
    elif current_risk < risk_map[(x, y)]:
        risk_map[(x, y)] = current_risk

    if (x, y) == (max_x, max_y):
        return

    if y + 1 <= max_y:
        compute(
            current_risk + data[y + 1][x],
            x,
            y + 1,
        )
    if x + 1 <= max_x:
        compute(
            current_risk + data[y][x + 1],
            x + 1,
            y,
        )
    if y - 1 >= 0:
        compute(
            current_risk + data[y - 1][x],
            x,
            y - 1,
        )
    if x - 1 >= 0:
        compute(
            current_risk + data[y][x - 1],
            x - 1,
            y,
        )


compute(
    0,
    0,
    0,
)
print(f"Answer part one: {risk_map[(max_x, max_y)]}")

from itertools import product

data = [[int((a := line.split(": "))[0]), a[1].split()] for line in open("input").read().splitlines()]


def solve(operators):
    res = 0
    for r, v in data:
        for c in product(operators, repeat=len(v) - 1):
            tmp = v[0]
            for i, x in enumerate(c):
                tmp = eval(str(tmp) + x + v[i + 1])
            if tmp == r:
                res += r
                break
    return res


print(f"Answer part one: {solve(("+", "*"))}")
print(f"Answer part two: {solve(("+", "*", ""))}")

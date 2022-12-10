polymer = open("input").read().splitlines()[0]


def solve(poly):
    i = 0
    res = list(poly)
    while i < len(res) - 1:
        if res[i] != res[i + 1] and res[i].lower() == res[i + 1].lower():
            del res[i]
            del res[i]
            if i > 0:
                i -= 1
        else:
            i += 1

    return res


print(f"Answer part one: {len(solve(polymer))}")

part_2 = min(len(solve(polymer.replace(c, "").replace(c.upper(), ""))) for c in set(polymer.lower()))
print(f"Answer part two: {part_2}")

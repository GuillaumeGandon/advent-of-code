cards = {
    i + 1: tuple(set(int(v) for v in x.split()) for x in line.split(": ")[1].split(" | "))
    for i, line in enumerate(open("input").read().splitlines())
}

intersections = (set.intersection(*x) for x in cards.values())

factor = {k: 1 for k in cards}
for k, (c, r) in cards.items():
    for i in range(k, k + len(c.intersection(r))):
        factor[i + 1] += factor[k]

print(f"Answer part one: {sum(2 ** (len(i) - 1) for i in intersections if i)}")
print(f"Answer part two: {sum(factor.values())}")

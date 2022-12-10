raw = open("input").read().splitlines()
data = tuple((row[0 : int(len(row) / 2)], row[int(len(row) / 2) :]) for row in raw)

errors = (set(x).intersection(set(y)).pop() for x, y in data)
badges = (set.intersection(set(raw[i]), set(raw[i + 1]), set(raw[i + 2])).pop() for i in range(0, len(raw), 3))


def sum_priorities(items):
    return sum(ord(i) - 38 if i.isupper() else ord(i) - 96 for i in items)


print(f"Answer part one: {sum_priorities(errors)}")
print(f"Answer part two: {sum_priorities(badges)}")

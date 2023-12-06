from math import prod

MOVES = (-1, 1, -1 - 1j, -1j, 1 - 1j, -1 + 1j, 1j, 1 + 1j)

lines = open("input").read().splitlines()

symbols = set(x + y * 1j for y, line in enumerate(lines) for x, c in enumerate(line) if c not in "01234566789.")
star_symbols = set(x + y * 1j for y, line in enumerate(lines) for x, c in enumerate(line) if c == "*")

numbers = {}
for y, line in enumerate(lines):
    pos = []
    number = ""
    for x, c in enumerate(line):
        if c.isdigit():
            pos.append(x + y * 1j)
            number += c
        elif number:
            numbers[tuple(pos)] = int(number)
            pos = []
            number = ""
    if number:
        numbers[tuple(pos)] = int(number)


part_1 = sum(v for k, v in numbers.items() if any(p + m in symbols for p in k for m in MOVES))
part_2 = 0
for s in star_symbols:
    a = tuple(v for k, v in numbers.items() if any(s + m in k for m in MOVES))
    if len(a) == 2:
        part_2 += prod(a)

print(f"Answer part one: {part_1}")
print(f"Answer part two: {part_2}")

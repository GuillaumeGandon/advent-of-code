from itertools import permutations

data = tuple(tuple(map(int, row.split("\t"))) for row in open("input").read().splitlines())
answer_part_one = sum(max(row) - min(row) for row in data)
print(f"Answer part one: {answer_part_one}")

answer_part_two = sum(a // b for row in data for a, b in permutations(row, 2) if a / b == a // b)
print(f"Answer part two: {answer_part_two}")

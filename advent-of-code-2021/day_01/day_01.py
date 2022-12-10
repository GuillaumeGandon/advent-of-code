input = tuple(map(int, open("input").read().splitlines()))

part_1 = sum(1 for i in range(1, len(input)) if input[i] > input[i - 1])
print(f"Answer part one: {part_1}")

part_2 = sum(1 for i in range(3, len(input)) if sum(input[i - 2 : i + 1]) > sum(input[i - 3 : i]))
print(f"Answer part two: {part_2}")

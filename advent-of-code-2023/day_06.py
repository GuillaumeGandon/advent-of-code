from math import prod


def compute_distance(hold_time, time):
    return (time - hold_time) * hold_time


times, distances = tuple(
    tuple(map(int, line.split(":")[1].strip().split())) for line in open("input").read().splitlines()
)


part_1 = prod(sum(compute_distance(i + 1, t) > d for i in range(t)) for t, d in zip(times, distances))
part_2 = sum(compute_distance(i + 1, 53837288) > 333163512891532 for i in range(53837288))

print(f"Answer part one: {part_1}")
print(f"Answer part two: {part_2}")

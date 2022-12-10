from math import copysign

motions = tuple(((x := row.split())[0], int(x[1])) for row in open("input").read().splitlines())


def same_row_or_column(head, tail):
    return head.real == tail.real or head.imag == tail.imag


def close_distance_diagonally(source, target):
    dist = target - source
    return copysign(1, dist.real) + 1j * copysign(1, dist.imag)


def simulate_rope(rope_length):
    rope = [0 + 0j] * rope_length
    mapping = {"R": 1, "L": -1, "U": 0 - 1j, "D": 0 + 1j}
    tail_visited_positions = set()
    for move, steps in motions:
        for _ in range(steps):
            for i in range(len(rope)):
                if i == 0:
                    rope[i] += mapping[move]
                else:
                    if abs(rope[i - 1] - rope[i]) == 2 and same_row_or_column(rope[i - 1], rope[i]):
                        rope[i] += (rope[i - 1] - rope[i]) / 2
                    elif abs(rope[i - 1] - rope[i]) > 2:
                        rope[i] += close_distance_diagonally(rope[i], rope[i - 1])
            tail_visited_positions.add(rope[-1])
    return tail_visited_positions


print(f"Answer part one: {len(simulate_rope(2))}")
print(f"Answer part two: {len(simulate_rope(10))}")

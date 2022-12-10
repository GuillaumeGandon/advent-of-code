TIME_LIMIT = 2503


def split_row(row):
    tmp = row.split()
    return int(tmp[3]), int(tmp[6]), int(tmp[-2])


def get_distance(deer, seconds):
    speed, speed_duration, rest = deer
    flying_time = seconds % (speed_duration + rest)
    if flying_time > speed_duration:
        flying_time = speed_duration
    flying_time += seconds // (speed_duration + rest) * speed_duration
    return speed * flying_time


reindeer = tuple(map(split_row, open('input').read().splitlines()))

max_distances = tuple(
    max(get_distance(deer, i + 1) for deer in reindeer)
    for i in range(TIME_LIMIT)
)

print(f"Answer part one: {max_distances[TIME_LIMIT - 1]}")

max_reindeer_points = max(
    sum(1 if max_distances[i] == get_distance(deer, i + 1) else 0
        for i in range(TIME_LIMIT))
    for deer in reindeer
)

print(f"Answer part two: {max_reindeer_points}")

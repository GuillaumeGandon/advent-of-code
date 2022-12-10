from collections import defaultdict

entries = sorted(
    (
        (((row_splitted := row.split())[0][1:], row_splitted[1]), " ".join(row_splitted[2:]))
        for row in open("input").read().splitlines()
    ),
    key=lambda x: x[0],
)


guards_sleep = defaultdict(lambda: defaultdict(lambda: 0))
current_guard = None
sleep_start = 0
for (date, hour_minute), status in entries:
    minute = int(hour_minute.split(":")[1][0:-1])
    if "Guard" in status:
        current_guard = int(status.split()[1].replace("#", ""))
    elif status == "falls asleep":
        sleep_start = minute
    else:
        for i in range(sleep_start, minute):
            guards_sleep[current_guard][i] += 1

max_total_asleep, max_minute_asleep = 0, 0
id_strat_1, minute_strat_1 = 0, 0
id_strat_2, minute_strat_2 = 0, 0
for id, sleep in guards_sleep.items():
    current_total_sleep = sum(sleep.values())
    current_max_minute = max(sleep.values())
    if current_total_sleep > max_total_asleep:
        id_strat_1 = id
        max_total_asleep = current_total_sleep
        minute_strat_1 = {v: k for k, v in sleep.items()}[current_max_minute]

    if current_max_minute > max_minute_asleep:
        id_strat_2 = id
        max_minute_asleep = current_max_minute
        minute_strat_2 = {v: k for k, v in sleep.items()}[max_minute_asleep]


print(f"Answer part one: {id_strat_1 * minute_strat_1}")
print(f"Answer part two: {id_strat_2 * minute_strat_2}")

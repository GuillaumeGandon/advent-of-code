from collections import deque


def find_trail_score(start, part_2=False):
    queue = deque([[start, {start}]])
    nb_distinct = 0
    ends = set()

    while queue:
        pos, seen = queue.popleft()
        for m in (1, -1, 1j, -1j):
            if pos + m in map and map[pos] + 1 == map[pos + m]:
                if map[pos + m] == 9:
                    ends.add(pos + m)
                    nb_distinct += 1
                else:
                    queue.append((pos + m, seen.union({pos + m})))

    if part_2:
        return nb_distinct
    return len(ends)


map = {(x + y * 1j): int(v) for y, line in enumerate(open("input").read().splitlines()) for x, v in enumerate(line)}
trailheads = [k for k, v in map.items() if v == 0]

print(f"Answer part one: {sum(find_trail_score(trailhead) for trailhead in trailheads)}")
print(f"Answer part two: {sum(find_trail_score(trailhead, part_2=True) for trailhead in trailheads)}")

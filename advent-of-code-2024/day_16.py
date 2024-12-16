from collections import deque

map = {
    (x + y * 1j): c for y, line in enumerate(open("input").read().splitlines()) for x, c in enumerate(line) if c != "#"
}
start = [k for k, v in map.items() if v == "S"][0]
end = [k for k, v in map.items() if v == "E"][0]


queue = deque(((start, 1, 0, set((start,))),))
best_score = {}
possible_paths = {}
while queue:
    p, direction, score, seen = queue.popleft()

    if (p, direction) in best_score and score > best_score[(p, direction)]:
        continue
    best_score[(p, direction)] = score
    if p == end:
        if score not in possible_paths:
            possible_paths[score] = []
        possible_paths[score].append(seen)
        continue
    for m in (1, -1, 1j, -1j):
        if p + m in map:
            if m != direction:
                queue.append((p + m, m, score + 1001, seen.union(set((p + m,)))))
            else:
                queue.appendleft((p + m, m, score + 1, seen.union(set((p + m,)))))
res = float("inf")
for m in (1, -1, 1j, -1j):
    if (end, m) in best_score and best_score[(end, m)] < res:
        res = best_score[(end, m)]

print(f"Answer part one: {res}")
print(f"Answer part two: {len(set.union(*possible_paths[res]))}")

from collections import deque


def solve(nb_bytes):
    bytes = {(x + y * 1j) for x, y in all_bytes[:nb_bytes]}
    queue = deque(([0, 0],))
    bests = dict()
    while 1:

        p, nb_steps = queue.popleft()
        if p not in bests or p in bests and nb_steps < bests[p]:
            bests[p] = nb_steps
        else:
            continue

        if p == R + R * 1j:
            return nb_steps
        for m in (-1, 1j, 1, -1j):
            if 0 <= (p + m).imag < R + 1 and 0 <= (p + m).real < R + 1 and p + m not in bytes:
                queue.append([p + m, nb_steps + 1])


R = 70
all_bytes = [list(map(int, line.split(","))) for line in open("input").read().splitlines()]

print(f"Answer part one: {solve(1024)}")

for i in range(1024, len(all_bytes)):
    try:
        solve(i)
    except:
        print(f"Answer part two: {all_bytes[i - 1][0]},{all_bytes[i - 1][1]}")
        break

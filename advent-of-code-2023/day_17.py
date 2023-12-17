from collections import deque, defaultdict


lines = open("input").read().splitlines()

H = len(lines)
W = len(lines[0])

grid = {(x + y * 1j): int(lines[y][x]) for y in range(H) for x in range(W)}
start = 0
end = (W - 1) + (H - 1) * 1j


def solve(part_2=False):
    seen = defaultdict(lambda: float("inf"))
    queue = deque(((start, 1, 0), (start, 1j, 0)))

    while queue:
        p, d, h = queue.popleft()
        if h < seen[(p, d)] and h < min(seen[(end, 1)], seen[(end, 1j)]):
            seen[(p, d)] = h

            for n_d in (d * 1j, d * -1j):
                n_p = p
                n_h = h
                for i in range(3 if not part_2 else 10):
                    n_p += n_d
                    if 0 <= n_p.real < W and 0 <= n_p.imag < H:
                        n_h += grid[n_p]
                        if not part_2 or i >= 3:
                            queue.append((n_p, n_d, n_h))
                    else:
                        break

    return min(seen[(end, 1)], seen[(end, 1j)])


print(f"Answer part one: {solve()}")
print(f"Answer part two: {solve(part_2=True)}")

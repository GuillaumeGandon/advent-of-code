from collections import deque
from itertools import chain

MIRROR = {1: -1j, -1: 1j, 1j: -1, -1j: 1}


def solve(start):
    queue = deque((start,))
    energized = set()

    while queue:
        p, d = queue.popleft()
        while 0 <= p.real < W and 0 <= p.imag < H and not (p, d) in energized:
            energized.add((p, d))
            if contraption[p] == "-" and d.real == 0:
                queue.extend(((p + 1, 1), (p - 1, -1)))
                break
            elif contraption[p] == "|" and d.imag == 0:
                queue.extend(((p + 1j, 1j), (p - 1j, -1j)))
                break
            elif contraption[p] == "/":
                d = MIRROR[d]
            elif contraption[p] == "\\":
                d = -MIRROR[d]
            p += d
    return len(set(p for p, _ in energized))


lines = open("input").read().splitlines()
H = len(lines)
W = len(lines[0])
contraption = {x + y * 1j: lines[y][x] for y in range(H) for x in range(W)}

print(f"Answer part one: {solve((0, 1))}")

queue_h = ((x + h, d) for h, d in ((0, 1j), ((H - 1) * 1j, -1j)) for x in range(W))
queue_v = ((w + y * 1j, d) for w, d in ((0, 1), (W - 1, -1)) for y in range(H))
print(f"Answer part two: {max(solve(queue) for queue in chain(queue_h, queue_v))}")

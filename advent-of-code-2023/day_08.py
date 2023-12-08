from math import gcd


def lcm(xs):
    ans = 1
    for x in xs:
        ans = (x * ans) // gcd(x, ans)
    return ans


lines = open("input").read().splitlines()

instructions = tuple(0 if c == "L" else 1 for c in lines[0])

maps = {(a := line.split(" = "))[0]: a[1][1:-1].split(", ") for line in lines[2:]}


def solve(start, end):
    all_current_pos = [p for p in maps if p.endswith(start)]
    nb_steps = 0
    step_win = [None] * len(all_current_pos)
    while not all(step_win):
        for i, p in enumerate(all_current_pos):
            all_current_pos[i] = maps[p][instructions[nb_steps % len(instructions)]]
            if step_win[i] is None and all_current_pos[i].endswith(end):
                step_win[i] = nb_steps + 1

        nb_steps += 1

    return lcm(step_win)


print(f"Answer part one: {solve('AAA', 'ZZZ')}")
print(f"Answer part two: {solve('A', 'Z')}")

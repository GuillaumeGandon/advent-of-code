def move_robots():
    for r in robots:
        ((x, y), (vx, vy)) = robots[r]
        if 0 <= vx + x < WIDE:
            x = vx + x
        elif vx + x < 0:
            x = WIDE + vx + x
        else:
            x = vx + x - WIDE

        if 0 <= vy + y < TALL:
            y = vy + y
        elif vy + y < 0:
            y = TALL + vy + y
        else:
            y = vy + y - TALL

        robots[r] = [[x, y], [vx, vy]]


def is_christmas_tree():
    robots_pos = {(x, y) for ((x, y), (vx, vy)) in robots.values()}
    lines = ""
    possible_tree = False
    for yy in range(TALL):
        line = ""
        for xx in range(WIDE):
            if (yy, xx) in robots_pos:
                line += "#"
            else:
                line += " "
        lines += line + "\n"
        if line.split() and max(len(x) for x in line.split()) >= 10:
            possible_tree = True
    if possible_tree:
        # print(lines)
        return True
    return False


WIDE = 101
TALL = 103

robots = {}
for i, line in enumerate(open("input").read().splitlines()):
    p, v = line.split()
    p, v = p[2:], v[2:]
    x, y = list(map(int, p.split(",")))
    vx, vy = list(map(int, v.split(",")))
    robots[i] = [[x, y], [vx, vy]]

i = 0
while 1:
    i += 1
    move_robots()
    if i == 100:
        first_quadrant = sum(x < WIDE // 2 and y < TALL // 2 for ((x, y), (vx, vy)) in robots.values())
        second_quadrant = sum(x > WIDE // 2 and y < TALL // 2 for ((x, y), (vx, vy)) in robots.values())
        third_quadrant = sum(x < WIDE // 2 and y > TALL // 2 for ((x, y), (vx, vy)) in robots.values())
        fourth_quadrant = sum(x > WIDE // 2 and y > TALL // 2 for ((x, y), (vx, vy)) in robots.values())

        print(f"Answer part one: {first_quadrant * second_quadrant * third_quadrant * fourth_quadrant}")
    if is_christmas_tree():
        print(f"Answer part two: {i}")
        break

def split_row(row):
    action_and_x1_y1, x2_y2 = row.split(' through ')
    action_and_x1_y1 = action_and_x1_y1.split(' ')
    x1_y1 = action_and_x1_y1[-1]
    if len(action_and_x1_y1) == 3:
        action = action_and_x1_y1[1]
    else:
        action = action_and_x1_y1[0]
    x1, y1 = tuple(int(x) for x in x1_y1.split(','))
    x2, y2 = tuple(int(x) for x in x2_y2.split(','))
    return action, x1, y1, x2, y2


def set_lights(lights, action, x1, y1, x2, y2):
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            pos = x + y * 1000
            if action == 'off':
                lights[pos] = False
            elif action == 'on':
                lights[pos] = True
            else:
                lights[pos] = not lights[pos]
    return lights


def set_lights_with_brightness(lights, action, x1, y1, x2, y2):
    for y in range(y1, y2 + 1):
        for x in range(x1, x2 + 1):
            pos = x + y * 1000
            if action == 'off':
                if lights[pos] != 0:
                    lights[pos] -= 1
            elif action == 'on':
                lights[pos] += 1
            else:
                lights[pos] += 2

    return lights


rows = tuple(map(split_row, open('input').read().splitlines()))

light_grid = [False] * 1_000_000
for row in rows:
    light_grid = set_lights(light_grid, *row)
print(f"Answer part one: {len(tuple(l for l in light_grid if l))}")

light_grid = [0] * 1_000_000
for row in rows:
    light_grid = set_lights_with_brightness(light_grid, *row)
print(f"Answer part two: {sum(light_grid)}")

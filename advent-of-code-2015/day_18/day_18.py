def count_neighbors(lights, light_idx, corner_stuck_on):
    x_list = y_list = (-1, 0, 1)
    if light_idx % GRID_SIZE == 0:
        x_list = (0, 1)
    elif light_idx % GRID_SIZE == GRID_SIZE - 1:
        x_list = (-1, 0)
    if light_idx // GRID_SIZE == 0:
        y_list = (0, 1)
    elif light_idx // GRID_SIZE == GRID_SIZE - 1:
        y_list = (-1, 0)

    return sum(
        1
        for x in x_list
        for y in y_list
        if (
                (l := (light_idx + x) + GRID_SIZE * y) >= 0 and
                l < LIGHTS_NUMBER and
                (lights[l] or corner_stuck_on and l in CORNERS) and
                l != light_idx
        )
    )


def compute_light_state(lights, light_idx, corner_stuck_on):
    if corner_stuck_on and light_idx in CORNERS:
        return True

    light_state = lights[light_idx]
    count = count_neighbors(lights, light_idx, corner_stuck_on)

    if light_state and count not in (2, 3):
        return False
    if not light_state and count == 3:
        return True
    return light_state


def compute_steps(input_lights, n_steps, corner_stuck_on=False):
    tmp = input_lights
    for i in range(n_steps):
        tmp = tuple(compute_light_state(tmp, i, corner_stuck_on) for i in range(LIGHTS_NUMBER))

    return tuple(light_state for light_state in tmp if light_state)


rows = open('input').read().splitlines()
GRID_SIZE = len(rows[0])
LIGHTS_NUMBER = GRID_SIZE ** 2
CORNERS = (0, GRID_SIZE - 1, GRID_SIZE * (GRID_SIZE - 1), GRID_SIZE ** 2 - 1)

initial_lights = tuple(c == '#' for row in rows for c in row)

print(f"Answer part one: {len(compute_steps(initial_lights, 100))}")
print(f"Answer part two: {len(compute_steps(initial_lights, 100, corner_stuck_on=True))}")

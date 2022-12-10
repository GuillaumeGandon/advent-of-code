instructions = list(map(int, open("input").read().splitlines()))


def find_maze_exit(inst, part_two=False):
    len_instructions = len(inst)
    position = 0
    step_nb = 0
    while 0 <= position < len_instructions:
        tmp = position
        position += inst[position]
        if part_two and inst[tmp] >= 3:
            inst[tmp] -= 1
        else:
            inst[tmp] += 1
        step_nb += 1
    return step_nb


print(f"Answer part one: {find_maze_exit(instructions.copy())}")
print(f"Answer part two: {find_maze_exit(instructions.copy(), part_two=True)}")

board_map, instructions = open("input").read().split("\n\n")

board_map = {(x + y * 1j): v for y, row in enumerate(board_map.splitlines()) for x, v in enumerate(row) if v != " "}
instructions = instructions.strip().replace("R", " R ").replace("L", " L ").split()


def solve():
    position = int(min(k.real for k in board_map if k.imag == 0))
    direction = 1
    for instruction in instructions:
        try:
            nb_steps = int(instruction)
            next_p = position
            for i in range(nb_steps):
                next_p += direction
                if next_p in board_map:
                    if board_map[next_p] == ".":
                        position = next_p
                    else:
                        break
                else:
                    if direction == 1:
                        wrap_position = int(min(k.real for k in board_map if k.imag == next_p.imag)) + next_p.imag * 1j
                    elif direction == -1:
                        wrap_position = int(max(k.real for k in board_map if k.imag == next_p.imag)) + next_p.imag * 1j
                    elif direction == 1j:
                        wrap_position = int(min(k.imag for k in board_map if k.real == next_p.real)) * 1j + next_p.real
                    else:
                        wrap_position = int(max(k.imag for k in board_map if k.real == next_p.real)) * 1j + next_p.real

                    if board_map[wrap_position] == ".":
                        next_p = wrap_position
                        position = next_p

        except:
            turn = instruction
            if turn == "L":
                direction *= -1j
            else:
                direction *= 1j

    if direction == 1:
        facing = 0
    elif direction == 1j:
        facing = 1
    elif direction == -1:
        facing = 2
    else:
        facing = 3
    return int((1000 * (position.imag + 1)) + (4 * (position.real + 1)) + facing)


print(f"Answer part one: {solve()}")
print(f"Answer part two: {None}")

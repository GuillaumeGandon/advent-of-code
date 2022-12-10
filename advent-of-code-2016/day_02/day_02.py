DIRECTIONS = {"U": 1j, "D": -1j, "L": -1, "R": +1}

KEYPAD = {
    (-1 + 1j): "1",
    (0 + 1j): "2",
    (1 + 1j): "3",
    (-1 + 0j): "4",
    (0 + 0j): "5",
    (1 + 0j): "6",
    (-1 - 1j): "7",
    (0 - 1j): "8",
    (1 - 1j): "9",
}

KEYPAD_2 = {
    (0 + 2j): "1",
    (-1 + 1j): "2",
    (0 + 1j): "3",
    (1 + 1j): "4",
    (-2 + 0j): "5",
    (-1 + 0j): "6",
    (0 + 0j): "7",
    (1 + 0j): "8",
    (2 + 0j): "9",
    (-1 - 1j): "A",
    (0 - 1j): "B",
    (1 - 1j): "C",
    (0 - 2j): "D",
}


def get_bathroom_code(position, keypad):
    bathroom_code = []
    for instruction in instructions:
        for direction in instruction:
            if position + DIRECTIONS[direction] in keypad:
                position += DIRECTIONS[direction]
        bathroom_code.append(keypad[position])
    return "".join(bathroom_code)


instructions = open("input").read().splitlines()

print(f"Answer part one: {get_bathroom_code(position=(0 + 0j), keypad=KEYPAD)}")
print(f"Answer part two: {get_bathroom_code(position=(-2 + 0j), keypad=KEYPAD_2)}")

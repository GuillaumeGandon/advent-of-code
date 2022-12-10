def compute():
    x, y, y_part_two = 0, 0, 0

    for inst, value in (line.split(" ") for line in open("input").read().splitlines()):
        if inst == "forward":
            x += int(value)
            y_part_two += int(value) * y
        elif inst == "down":
            y += int(value)
        else:
            y -= int(value)

    return x * y, x * y_part_two


part_one, part_two = compute()
print(f"Answer part one: {part_one}")
print(f"Answer part two: {part_two}")

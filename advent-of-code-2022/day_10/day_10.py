register_x = 1
register_values = []
for row in open("input").read().splitlines():
    register_values.append(register_x)
    if row != "noop":
        register_values.append(register_x)
        register_x += int(row.split()[1])


print(f"Answer part one: {sum(i * register_values[i - 1] for i in range(20, len(register_values), 40))}")

print("Answer part two:")
line = ""
for cycle, x in enumerate(register_values):
    if x <= (cycle + 1) % 40 <= x + 2:
        line += "██"
    else:
        line += "  "
    if (cycle + 1) % 40 == 0:
        print(line)
        line = ""

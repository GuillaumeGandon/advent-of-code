registers = {}
all_time_max = -float("inf")

for modify, condition in (tuple(line.split(" if ")) for line in open("input").read().splitlines()):
    register_condition = condition.split(" ")[0]
    if register_condition not in registers:
        registers[register_condition] = 0

    condition = condition.replace(register_condition, str(registers[register_condition]))

    if eval(condition):
        register, operation, value = modify.split(" ")
        if register not in registers:
            registers[register] = 0
        if operation == "inc":
            registers[register] += int(value)
        else:
            registers[register] -= int(value)

        all_time_max = max(all_time_max, registers[register])

print(f"Answer part one: {max(registers.values())}")
print(f"Answer part two: {all_time_max}")

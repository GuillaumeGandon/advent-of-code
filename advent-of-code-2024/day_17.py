def get_combo_operand(operand):
    if operand == 4:
        return A
    if operand == 5:
        return B
    if operand == 6:
        return C
    return operand


a, b = open("input").read().split("\n\n")
A, B, C = [int(line.split(": ")[-1]) for line in a.splitlines()]
program = list(map(int, b.split(": ")[-1].strip().split(",")))

instruction_pointer = 0
output = ""
while 0 <= instruction_pointer < len(program):
    opcode, operand = program[instruction_pointer : instruction_pointer + 2]

    if opcode == 0:
        A //= 2 ** get_combo_operand(operand)
    elif opcode == 1:
        B ^= operand
    elif opcode == 2:
        B = get_combo_operand(operand) % 8
    elif opcode == 3:
        if A != 0:
            instruction_pointer = operand
            continue
    elif opcode == 4:
        B ^= C
    elif opcode == 5:
        output += str(get_combo_operand(operand) % 8)
    elif opcode == 6:
        B = A // (2 ** get_combo_operand(operand))
    elif opcode == 7:
        C = A // (2 ** get_combo_operand(operand))

    instruction_pointer += 2

print(",".join(output))

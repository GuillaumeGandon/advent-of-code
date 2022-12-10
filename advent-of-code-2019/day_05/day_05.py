ADD = 1
MULT = 2

INPUT = 3
OUTPUT = 4

JUMP_IF_TRUE = 5
JUMP_IF_FALSE = 6
LESS_THAN = 7
EQUALS = 8

HALT = 99

NOUN = 1
VERB = 2


def decode_instruction(mem, i):
    opcode, mode_1, mode_2, mode_3 = get_mode(mem[i])
    # print(i, mem)
    # print(mem[i], opcode, mode_1, mode_2, mode_3)
    p1, p2, p3 = None, None, None

    if opcode in [ADD, MULT, INPUT, OUTPUT, JUMP_IF_TRUE, JUMP_IF_FALSE, LESS_THAN, EQUALS]:
        p1 = mem[i + NOUN]
        if not mode_1:
            p1 = mem[p1]

    if opcode in [ADD, MULT, JUMP_IF_TRUE, JUMP_IF_FALSE, LESS_THAN, EQUALS]:
        p2 = mem[i + VERB]
        if not mode_2:
            p2 = mem[p2]

    if opcode == INPUT:
        p3 = mem[i + 1]
    elif opcode in [ADD, MULT, LESS_THAN, EQUALS]:
        p3 = mem[i + 3]

    return opcode, p1, p2, p3


def get_mode(value):
    s = str(value)
    opcode = int(s[-2:])
    mode_1 = len(s) >= 3 and s[-3] == '1'
    mode_2 = len(s) >= 4 and s[-4] == '1'
    mode_3 = len(s) >= 5 and s[-5] == '1'
    if mode_3:
        print('fail')
    return opcode, mode_1, mode_2, mode_3


def run_intcode(memory, input_value):
    mem = memory.copy()
    final_ouput = None
    i = 0
    while 1:
        opcode, p1, p2, p3 = decode_instruction(mem, i)

        if opcode == ADD:
            mem[p3] = p1 + p2
            i += 4
        elif opcode == MULT:
            mem[p3] = p1 * p2
            i += 4
        elif opcode == INPUT:
            mem[p3] = input_value
            i += 2
        elif opcode == OUTPUT:
            # print(p1)
            final_ouput = p1
            i += 2
        elif opcode == JUMP_IF_TRUE:
            if p1:
                i = p2
            else:
                i += 3
        elif opcode == JUMP_IF_FALSE:
            if not p1:
                i = p2
            else:
                i += 3
        elif opcode == LESS_THAN:
            if p1 < p2:
                mem[p3] = 1
            else:
                mem[p3] = 0
            i += 4
        elif opcode == EQUALS:
            if p1 == p2:
                mem[p3] = 1
            else:
                mem[p3] = 0
            i += 4
        elif opcode == HALT:
            break
        else:
            print('fail')
            break
    return final_ouput


input_mem = list(map(int, open('input').read().strip().split(',')))

print(f'Answer part one: {run_intcode(input_mem, 1)}')
print(f'Answer part two: {run_intcode(input_mem, 5)}')

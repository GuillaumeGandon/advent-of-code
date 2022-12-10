from itertools import permutations

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


class Amplifier:
    def __init__(self, memory, inputs):
        self.mem = memory
        self.inputs = inputs
        self.output = None

    def run_intcode(self):
        final_output = None
        i = 0
        while 1:
            opcode, p1, p2, p3 = decode_instruction(self.mem, i)

            if opcode == ADD:
                self.mem[p3] = p1 + p2
                i += 4
            elif opcode == MULT:
                self.mem[p3] = p1 * p2
                i += 4
            elif opcode == INPUT:
                self.mem[p3] = self.inputs.pop(0)
                # print(f'input: {self.mem[p3]}')
                i += 2
            elif opcode == OUTPUT:
                # print(f'ouput: {p1}')
                final_output = p1
                i += 2
                yield p1
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
                    self.mem[p3] = 1
                else:
                    self.mem[p3] = 0
                i += 4
            elif opcode == EQUALS:
                if p1 == p2:
                    self.mem[p3] = 1
                else:
                    self.mem[p3] = 0
                i += 4
            elif opcode == HALT:
                break
            else:
                print('fail')
                break
        return final_output


def run_amplifier(a, b, c, d, e):
    output_a = next(Amplifier(input_mem, [a, 0]).run_intcode())
    output_b = next(Amplifier(input_mem, [b, output_a]).run_intcode())
    output_c = next(Amplifier(input_mem, [c, output_b]).run_intcode())
    output_d = next(Amplifier(input_mem, [d, output_c]).run_intcode())
    return next(Amplifier(input_mem, [e, output_d]).run_intcode())


def run_amplifier_with_feed_back_loop(a, b, c, d, e):
    amp_a = Amplifier(input_mem, [a, 0])
    amp_b = Amplifier(input_mem, [b])
    amp_c = Amplifier(input_mem, [c])
    amp_d = Amplifier(input_mem, [d])
    amp_e = Amplifier(input_mem, [e])

    gen_a = amp_a.run_intcode()
    gen_b = amp_b.run_intcode()
    gen_c = amp_c.run_intcode()
    gen_d = amp_d.run_intcode()
    gen_e = amp_e.run_intcode()

    output = None
    while True:
        try:
            amp_b.inputs.append(next(gen_a))
            amp_c.inputs.append(next(gen_b))
            amp_d.inputs.append(next(gen_c))
            amp_e.inputs.append(next(gen_d))

            output = next(gen_e)
            amp_a.inputs.append(output)
        except StopIteration:
            break
    return output


input_mem = list(map(int, open('input').read().strip().split(',')))

max_thruster_signal_part_one = max(run_amplifier(*phases) for phases in permutations((0, 1, 2, 3, 4)))
print(f'Answer part one: {max_thruster_signal_part_one}')

max_thruster_signal_part_two = max(run_amplifier_with_feed_back_loop(*phases) for phases in permutations((5, 6, 7, 8, 9)))
print(f'Answer part two: {max_thruster_signal_part_two}')

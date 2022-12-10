def run_program(instructions, a=0, b=0):
    i = 0
    registers = {'a': a, 'b': b}

    while 0 <= i < len(instructions):
        inst = instructions[i]
        offset = 1
        if 'hlf' in inst:
            registers[inst[-1]] = registers[inst[-1]] // 2
        elif 'tpl' in inst:
            registers[inst[-1]] *= 3
        elif 'inc' in inst:
            registers[inst[-1]] += 1
        elif 'jmp' in inst:
            offset = int(inst.split(' ')[-1])
        elif 'jie' in inst:
            if registers[inst[4]] % 2 == 0:
                offset = int(inst[7:])
        elif 'jio' in inst:
            if registers[inst[4]] == 1:
                offset = int(inst[7:])
        i += offset
    return registers['b']


rows = open('input').read().splitlines()
print(f"Answer part one: {run_program(rows)}")
print(f"Answer part two: {run_program(rows, a=1)}")

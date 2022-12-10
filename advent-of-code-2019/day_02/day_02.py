from itertools import product

ADD = 1
MULT = 2
HALT = 99

NOUN = 1
VERB = 2


def run_intcode(memory):
    res = memory.copy()
    for i in range(0, len(res), 4):
        if res[i] == ADD:
            res[res[i + 3]] = res[res[i + NOUN]] + res[res[i + VERB]]
        elif res[i] == MULT:
            res[res[i + 3]] = res[res[i + NOUN]] * res[res[i + VERB]]
        elif res[i] == HALT:
            break
        else:
            print('fail')
    return res


input_mem = list(map(int, open('input').read().strip().split(',')))

input_mem[1] = 12
input_mem[2] = 2
print(f'Answer part one: {run_intcode(input_mem)[0]}')

for noun, verb in product(range(100), range(100)):
    mem = input_mem.copy()
    mem[NOUN], mem[VERB] = noun, verb
    if run_intcode(mem)[0] == 19690720:
        print(f'Answer part two: {100 * noun + verb}')
        break

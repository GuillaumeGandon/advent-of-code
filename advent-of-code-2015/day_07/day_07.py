from functools import cache


def split_row(row):
    instructions, output = row.split(' -> ')
    return output, tuple(instructions.split(' '))


@cache
def solve(key):
    if key.isdigit():
        return int(key)
    else:
        instructions = circuit[key]
        if len(instructions) == 1:
            return solve(instructions[0])
        elif len(instructions) == 2:
            gate, wire_or_signal = instructions
            return 65535 - solve(wire_or_signal)
        else:
            a, gate, b = instructions
            if gate == 'AND':
                return solve(a) & solve(b)
            elif gate == 'OR':
                return solve(a) | solve(b)
            elif gate == 'LSHIFT':
                return solve(a) << int(b)
            else:
                return solve(a) >> int(b)


circuit = dict(map(split_row, open('input').read().splitlines()))

print(f"Answer part one: {solve('a')}")

solve.cache_clear()
circuit['b'] = ('16076',)
print(f"Answer part two: {solve('a')}")

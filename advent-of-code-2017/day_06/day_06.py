memory = list(map(int, open("input").read().split("\t")))
memory_len = len(memory)

redistributions, nb_cycle = {}, 0

while tuple(memory) not in redistributions:
    redistributions[tuple(memory)] = nb_cycle
    nb_cycle += 1
    bank_with_most_blocks = memory.index(max(memory))
    blocks = memory[bank_with_most_blocks]
    memory[bank_with_most_blocks] = 0
    for i in range(blocks):
        memory[(bank_with_most_blocks + i + 1) % memory_len] += 1

print(f"Answer part one: {nb_cycle}")
print(f"Answer part two: {nb_cycle - redistributions[tuple(memory)]}")

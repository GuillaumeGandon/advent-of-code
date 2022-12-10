from copy import deepcopy

crates, procedure = open("input").read().split("\n\n")

nb_columns = int(crates[-2])

stacks = {
    i + 1: [row[1 + i * 4] for row in crates.splitlines()[:-1] if row[1 + i * 4] != " "] for i in range(nb_columns)
}

moves = tuple((int((x := row.split())[1]), int(x[3]), int(x[5])) for row in procedure.splitlines())


def solve(part_2=False):
    stacks_copy = deepcopy(stacks)
    for x, y, z in moves:
        tmp = stacks_copy[y][:x]
        if part_2:
            tmp = tmp[::-1]
        stacks_copy[y] = stacks_copy[y][x:]
        stacks_copy[z] = tmp + stacks_copy[z]

    return "".join(v[0] for v in stacks_copy.values())


print(f"Answer part one: {solve()}")
print(f"Answer part two: {solve(part_2=True)}")

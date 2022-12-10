ADJACENTS = ((-1 - 1j), (0 - 1j), (1 - 1j), (-1 + 0j), (1 + 0j), (-1 + 1j), (0 + 1j), (1 + 1j))


def compute_step():
    new_flashes = set()
    for k in octopuses:
        octopuses[k] += 1
        if octopuses[k] > 9:
            octopuses[k] = 0
            new_flashes.add(k)

    while new_flashes:
        for k in new_flashes:
            if octopuses[k] == 0:
                for adj in ADJACENTS:
                    if k + adj in octopuses and octopuses[k + adj] > 0:
                        octopuses[k + adj] += 1

        new_flashes = set()
        for k in octopuses:
            if octopuses[k] > 9:
                octopuses[k] = 0
                new_flashes.add(k)


def compute():
    flashes = 0
    step = 1
    while True:
        compute_step()
        flashes += sum(1 for v in octopuses.values() if v == 0)
        if step == 100:
            print(f"Answer part one: {flashes}")
        if all(v == 0 for v in octopuses.values()):
            print(f"Answer part two: {step}")
            break
        step += 1

    return flashes


input = tuple(tuple(map(int, line)) for line in open("input").read().splitlines())
octopuses = {(x + 1j * y): input[y][x] for y in range(len(input)) for x in range(len(input[0]))}
compute()

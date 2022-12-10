from copy import deepcopy
from os import system
from time import sleep

system("cls")

ADJACENTS = ((-1 - 1j), (0 - 1j), (1 - 1j), (-1 + 0j), (1 + 0j), (-1 + 1j), (0 + 1j), (1 + 1j))


def print_animation(step, flashes, part_one):
    tab = (
        ["\033c"]
        + list(
            "    "
            + "".join(
                str(octopuses[x + 1j * y] if octopuses[x + 1j * y] != 0 else f"\033[92m{octopuses[x + 1j * y]}\033[0m")
                for x in range(len(input[0]))
            )
            for y in range(len(input))
        )
        + ["\n"]
    )
    anim = deepcopy(tab)
    anim[1] += f"    \033[93mstep: {step}\033[0m"
    anim[3] += f"    \033[93mtotal flashes: {flashes}\033[0m"
    if part_one:
        if step <= 120 and step % 2 == 0:
            anim[5] += f"    \033[96manswer part one: {part_one}\033[0m"
        elif step <= 120 and step % 2 == 1:
            anim[5] += f"    \033[36manswer part one: {part_one}\033[0m"
        else:
            anim[5] += f"    \033[96manswer part one: {part_one}\033[0m"
    else:
        anim[5] += "    \033[96manswer part one: \033[0m"

    if all(v == 0 for v in octopuses.values()):
        for i in range(11):
            if i % 2 == 0:
                anim[7] = tab[7] + f"    \033[36manswer part two: {step}\033[0m"
            else:
                anim[7] = tab[7] + f"    \033[96manswer part two: {step}\033[0m"
            print("\n".join(anim))
            sleep(0.05)
    else:
        anim[7] += "    \033[36manswer part two: \033[0m"
        print("\n".join(anim))
        if step <= 10:
            sleep(1 - 0.95 * (step - 1) / 10)
        elif step <= 100:
            sleep(0.05)
        elif step <= 120:
            sleep(0.05 - 0.04 * (step - 100) / 20)
        else:
            sleep(0.01)


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
    part_one = None
    while True:
        compute_step()
        flashes += sum(1 for v in octopuses.values() if v == 0)
        print_animation(step, flashes, part_one)
        if step == 100:
            part_one = flashes
        if all(v == 0 for v in octopuses.values()):
            break
        step += 1

    return flashes


input = tuple(tuple(map(int, line)) for line in open("input").read().splitlines())
octopuses = {(x + 1j * y): input[y][x] for y in range(len(input)) for x in range(len(input[0]))}
compute()

from os import system
from time import sleep

instructions = open("input").read().splitlines()

display = [[" "] * 50 for _ in range(6)]


system("cls")


def print_display():
    lines = (
        "\033c\033[92m┏"
        + "━" * 50
        + "┓\n"
        + "".join("┃" + "".join(line) + "┃\n" for line in display)
        + "┗"
        + "━" * 50
        + "┛\n\033[0m"
    )
    print(lines)
    sleep(0.02)


def draw_rect(x, y):
    for i in range(x):
        for j in range(y):
            display[j][i] = "█"


def rotate_column(x, b):
    aa = [line[x] for line in display]
    bb = aa[-b:] + aa[:-b]
    for i, bbb in enumerate(bb):
        display[i][x] = bbb


def rotate_row(y, b):
    display[y] = display[y][-b:] + display[y][:-b]


print_display()

for instruction in instructions:
    if "rect" in instruction:
        x, y = list(map(int, instruction.split()[1].split("x")))
        draw_rect(x, y)
    elif "rotate column" in instruction:
        x = int(instruction.split()[2].split("=")[1])
        b = int(instruction.split()[-1])
        rotate_column(x, b)
    else:
        y = int(instruction.split()[2].split("=")[1])
        b = int(instruction.split()[-1])
        rotate_row(y, b)
    print_display()


part_one = sum(pixel == "█" for line in display for pixel in line)
print(f"\033[96mAnswer part one: {part_one}\033[0m")

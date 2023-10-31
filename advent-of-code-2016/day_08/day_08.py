instructions = open("input").read().splitlines()

display = [[" "] * 50 for _ in range(6)]


def print_display():
    for line in display:
        print("".join(line))


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


print(f"Answer part one: {sum(pixel == '█' for line in display for pixel in line)}")
print_display()

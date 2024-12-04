data = [line for line in open("input").read().splitlines()]


XMAS = "XMAS"
len_xmas = len(XMAS)
nb_lines = len(data)
nb_cols = len(data[0])
part_1 = 0

# horizontal: right
for y in range(nb_lines):
    for x in range(nb_cols - len_xmas + 1):
        if data[y][x] + data[y][x + 1] + data[y][x + 2] + data[y][x + 3] == XMAS:
            part_1 += 1


# horizontal: left
for y in range(nb_lines):
    for x in range(nb_cols - 1, 2, -1):
        if data[y][x] + data[y][x - 1] + data[y][x - 2] + data[y][x - 3] == XMAS:
            part_1 += 1

# vertical: down
for x in range(nb_cols):
    for y in range(nb_lines - len_xmas + 1):
        if data[y][x] + data[y + 1][x] + data[y + 2][x] + data[y + 3][x] == XMAS:
            part_1 += 1

# vertical: up
for x in range(nb_cols):
    for y in range(nb_lines - 1, 2, -1):
        if data[y][x] + data[y - 1][x] + data[y - 2][x] + data[y - 3][x] == XMAS:
            part_1 += 1

# Diag: down, right
for y in range(nb_lines - len_xmas + 1):
    for x in range(nb_cols - len_xmas + 1):
        if data[y][x] + data[y + 1][x + 1] + data[y + 2][x + 2] + data[y + 3][x + 3] == XMAS:
            part_1 += 1

# Diag: up, left
for y in range(nb_lines - 1, 2, -1):
    for x in range(nb_lines - 1, 2, -1):
        if data[y][x] + data[y - 1][x - 1] + data[y - 2][x - 2] + data[y - 3][x - 3] == XMAS:
            part_1 += 1

# Diag: down, left
for y in range(nb_lines - len_xmas + 1):
    for x in range(nb_lines - 1, 2, -1):
        if data[y][x] + data[y + 1][x - 1] + data[y + 2][x - 2] + data[y + 3][x - 3] == XMAS:
            part_1 += 1

# Diag: up, right
for y in range(nb_lines - 1, 2, -1):
    for x in range(nb_cols - len_xmas + 1):
        if data[y][x] + data[y - 1][x + 1] + data[y - 2][x + 2] + data[y - 3][x + 3] == XMAS:
            part_1 += 1

print(f"Answer part one: {part_1}")


def get_shape(x, y):
    return [data[y][x : x + 3], data[y + 1][x : x + 3], data[y + 2][x : x + 3]]


def is_mas_shape(b):
    return b[0][0] == "M" and b[0][2] == "S" and b[1][1] == "A" and b[2][0] == "M" and b[2][2] == "S"


def rotate_left(b):
    return [[b[y][x] for y in range(len(b))] for x in range(len(b[0]) - 1, -1, -1)]


part_2 = 0
for y in range(nb_lines - 2):
    for x in range(nb_cols - 2):
        b = get_shape(x, y)
        for i in range(4):
            b = rotate_left(b)
            if is_mas_shape(b):
                part_2 += 1

print(f"Answer part two: {part_2}")

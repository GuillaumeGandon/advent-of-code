import re

FIRST_CODE = 20151125
MULTIPLIER = 252533
DIVIDER = 33554393

targeted_row, targeted_col = map(int, re.findall(r'\d+', open('input').read()))

row, col = 1, 1
tmp = FIRST_CODE
while 1:
    if row == 1:
        row, col = col + 1, 1
    else:
        row -= 1
        col += 1

    tmp = tmp * MULTIPLIER % DIVIDER
    if row == targeted_row and col == targeted_col:
        print(f"Answer part one: {tmp}")
        break

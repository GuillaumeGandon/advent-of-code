from math import prod


def is_low_point(i, j):
    return (
        (i == 0 or i > 0 and input[i - 1][j] > input[i][j])
        and (i == nb_lines - 1 or i < nb_lines - 1 and input[i + 1][j] > input[i][j])
        and (j == 0 or j > 0 and input[i][j - 1] > input[i][j])
        and (j == len_line - 1 or j < len_line - 1 and input[i][j + 1] > input[i][j])
    )


def find_bassin(i, j, last, x=set()):
    if (i, j) not in x and 0 <= i < nb_lines and 0 <= j < len_line and input[i][j] != 9 and input[i][j] >= last:
        x.add((i, j))
        return (
            1
            + find_bassin(i - 1, j, input[i][j])
            + find_bassin(i + 1, j, input[i][j])
            + find_bassin(i, j - 1, input[i][j])
            + find_bassin(i, j + 1, input[i][j])
        )
    return 0


input = tuple(tuple(map(int, line)) for line in open("input").read().splitlines())

len_line = len(input[0])
nb_lines = len(input)

low_points = tuple((i, j) for i in range(nb_lines) for j in range(len_line) if is_low_point(i, j))
print(f"Answer part one: {sum(input[i][j] + 1 for i,j in low_points)}")


bassins = sorted(tuple(find_bassin(i, j, 0) for i, j in low_points), reverse=True)
print(f"Answer part two: {prod(bassins[:3])}")

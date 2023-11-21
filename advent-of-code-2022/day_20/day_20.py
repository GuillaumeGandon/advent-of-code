from copy import deepcopy

data = list(map(int, open("input").read().splitlines()))

DATA_LEN = len(data) - 1


numbers_dict = {}
for i, v in enumerate(data):
    if i == 0:
        numbers_dict[i] = [v, len(data) - 1, i + 1]
    elif i == len(data) - 1:
        numbers_dict[i] = [v, i - 1, 0]
    else:
        numbers_dict[i] = [v, i - 1, i + 1]


def groove_coordinate(nb, d):
    next = [k for k, v in d.items() if v[0] == 0][0]
    for i in range(nb):
        next = d[next][2]
    return d[next][0]


def solve(numbers, nb_mixing=1):
    d = deepcopy(numbers)
    if nb_mixing != 1:
        for k in d:
            d[k][0] *= 811589153
    start = 0
    for _id_mix in range(nb_mixing):
        for k in d.keys():
            value, last, next = d[k]
            if value == 0:
                continue
            else:
                d[last][2] = next
                d[next][1] = last

                if k == start:
                    start = next

                if value < 0:
                    new_next = k
                    for _i in range(abs(value) % DATA_LEN):
                        _v, new_next, _n = d[new_next]
                    new_last = d[new_next][1]
                else:
                    new_last = k
                    for _i in range(value % DATA_LEN):
                        _v, _l, new_last = d[new_last]
                    new_next = d[new_last][2]

                d[new_last][2] = k
                d[new_next][1] = k
                d[k][1] = new_last
                d[k][2] = new_next

    return sum(groove_coordinate(i, d) for i in (1000, 2000, 3000))


print(f"Answer part one: {solve(numbers_dict)}")
print(f"Answer part two: {solve(numbers_dict, nb_mixing=10)}")

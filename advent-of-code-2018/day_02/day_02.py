from collections import Counter
from math import prod

ids = open("input").read().splitlines()


def counts_two_and_three():
    return prod(
        map(
            sum,
            zip(
                *(
                    (1 if 2 in (counts := {v: k for k, v in Counter(id).items()}) else 0, 1 if 3 in counts else 0)
                    for id in ids
                )
            ),
        )
    )


def find_common_letters():
    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            if sum(1 for k, l in zip(ids[i], ids[j]) if k != l) == 1:
                return "".join(k for k, l in zip(ids[i], ids[j]) if k == l)


print(f"Answer part one: {counts_two_and_three()}")
print(f"Answer part two: {find_common_letters()}")

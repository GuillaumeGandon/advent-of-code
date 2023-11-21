from functools import cache
from math import prod

blueprints = tuple(
    tuple(map(int, ((x := row.split(" "))[6], x[12], x[18], x[21], x[27], x[30])))
    for row in open("input").read().splitlines()
)


def update_ressources(a, b, c, d, aa, bb, cc, dd):
    return (
        a + aa,
        b + bb,
        c + cc,
        d + dd,
        aa,
        bb,
        cc,
        dd,
    )


@cache
def find_max(nb_minutes, bp, ressources, can_build):

    res = 0

    ore, clay, obsidian, _d, _aa, _bb, _cc, _dd = ressources
    a1, b1, c1, d1, aa1, bb1, cc1, dd1 = update_ressources(*ressources)

    if nb_minutes - 1 == 0 or aa1 > max(bp[:2]) or bb1 > bp[3]:
        return d1

    if ore >= bp[0] and not can_build[0]:
        res = max(
            res, find_max(nb_minutes - 1, bp, (a1 - bp[0], b1, c1, d1, aa1 + 1, bb1, cc1, dd1), (False, False, False))
        )
    if ore >= bp[1] and not can_build[1]:
        res = max(
            res, find_max(nb_minutes - 1, bp, (a1 - bp[1], b1, c1, d1, aa1, bb1 + 1, cc1, dd1), (False, False, False))
        )
    if ore >= bp[2] and clay >= bp[3] and not can_build[2]:
        res = max(
            res,
            find_max(
                nb_minutes - 1, bp, (a1 - bp[2], b1 - bp[3], c1, d1, aa1, bb1, cc1 + 1, dd1), (False, False, False)
            ),
        )
    if ore >= bp[4] and obsidian >= bp[5]:
        res = max(
            res,
            find_max(
                nb_minutes - 1, bp, (a1 - bp[4], b1, c1 - bp[5], d1, aa1, bb1, cc1, dd1 + 1), (False, False, False)
            ),
        )
    else:
        res = max(
            res,
            find_max(
                nb_minutes - 1,
                bp,
                (a1, b1, c1, d1, aa1, bb1, cc1, dd1),
                (ore >= bp[0], ore >= bp[1], ore >= bp[2] and clay >= bp[3]),
            ),
        )
    return res


def solve(blueprints, nb_minutes):
    print(nb_minutes)
    res = []
    for bp in blueprints:
        res.append(find_max(nb_minutes, bp, (0, 0, 0, 0, 1, 0, 0, 0), (False, False, False)))
        print(res)
        find_max.cache_clear()
    return res


# print(f"Answer part one: {sum((i + 1) * x for i, x in enumerate(solve(blueprints, nb_minutes=24)))}")
# Answer part one: 1382
# real    1m30.016s


print(f"Answer part two: {prod(solve(blueprints[:3], nb_minutes=32))}")
# Answer part two: 31740
# nb_minutes=27    0m7.392s
# nb_minutes=32    15m51.673s

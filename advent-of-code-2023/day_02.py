from collections import defaultdict
from math import prod

lines = open("input").read().splitlines()

games = {i + 1: line.split(": ")[1] for i, line in enumerate(lines)}


def get_max_rgb_of_game(game):
    max_rgb = defaultdict(lambda: 0)
    for turn in game.split("; "):
        for cube in turn.split(", "):
            nb_cube, color = cube.split()
            if "red" in color:
                max_rgb["r"] = max(max_rgb["r"], int(nb_cube))
            elif "green" in color:
                max_rgb["g"] = max(max_rgb["g"], int(nb_cube))
            if "blue" in color:
                max_rgb["b"] = max(max_rgb["b"], int(nb_cube))
    return max_rgb


part_1 = sum(
    id
    for id, g in games.items()
    if (max_rgb := get_max_rgb_of_game(g))["r"] <= 12 and max_rgb["g"] <= 13 and max_rgb["b"] <= 14
)
part_2 = sum(prod(get_max_rgb_of_game(g).values()) for g in games.values())
print(f"Answer part one: {part_1}")
print(f"Answer part two: {part_2}")

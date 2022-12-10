mapping_1 = {
    "X": {"A": 1 + 3, "B": 1 + 0, "C": 1 + 6},
    "Y": {"A": 2 + 6, "B": 2 + 3, "C": 2 + 0},
    "Z": {"A": 3 + 0, "B": 3 + 6, "C": 3 + 3},
}

mapping_2 = {
    "X": {"A": "Z", "B": "X", "C": "Y"},
    "Y": {"A": "X", "B": "Y", "C": "Z"},
    "Z": {"A": "Y", "B": "Z", "C": "X"},
}

strategy_guide = tuple(row.split() for row in open("input").read().splitlines())


print(f"Answer part one: {sum(mapping_1[p2][p1] for p1, p2 in strategy_guide)}")
print(f"Answer part two: {sum(mapping_1[mapping_2[p2][p1]][p1] for p1, p2 in strategy_guide)}")

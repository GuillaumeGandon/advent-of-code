from itertools import combinations

rows = tuple(map(int, open('input').read().splitlines()))

valid_combinations = tuple(
    comb
    for i in range(len(rows))
    for comb in combinations(rows, i + 1)
    if sum(comb) == 150
)
print(f"Answer part one: {len(valid_combinations)}")

min_combination = min(map(len, valid_combinations))
print(f"Answer part two: {sum(1 for w in valid_combinations if len(w) == min_combination)}")

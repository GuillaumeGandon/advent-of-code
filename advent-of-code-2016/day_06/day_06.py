from collections import Counter

columns = tuple(zip(*open("input").read().splitlines()))

print(f"Answer part one: {''.join(Counter(col).most_common()[0][0] for col in columns)}")
print(f"Answer part two: {''.join(Counter(col).most_common()[-1][0] for col in columns)}")

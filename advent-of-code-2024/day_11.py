from collections import Counter, defaultdict


def count_changes(stones, nb_blinks):
    for _ in range(nb_blinks):
        new_stones = defaultdict(lambda: 0)
        for s, v in stones.items():
            if s == 0:
                new_stones[1] += v
            elif len(str(s)) % 2 == 0:
                a = int(str(s)[: len(str(s)) // 2])
                b = int(str(s)[len(str(s)) // 2 :])
                new_stones[a] += v
                new_stones[b] += v
            else:
                new_stones[s * 2024] += v
        stones = new_stones
    return sum(v for v in stones.values())


stones = Counter(list(map(int, open("input").read().split())))

print(f"Answer part one: {count_changes(stones, nb_blinks=25)}")
print(f"Answer part two: {count_changes(stones, nb_blinks=75)}")

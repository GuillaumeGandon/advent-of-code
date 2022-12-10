VOWELS = 'aeiou'
BAD_STRINGS = ['ab', 'cd', 'pq', 'xy']


def is_nice_string(row):
    if (
            sum(row.count(v) for v in VOWELS) >= 3 and
            any(row[i] == row[i + 1] for i in range(len(row) - 1)) and
            not any(b in row for b in BAD_STRINGS)
    ):
        return True
    return False


def is_nice_string_bis(row):
    if (
            any(row[i:i + 2] in row[i + 2:] for i in range(len(row) - 2)) and
            any(row[i] == row[i + 2] for i in range(len(row) - 2))
    ):
        return True
    return False


rows = open('input').read().splitlines()
print(f"Answer part one: {len(tuple(row for row in rows if is_nice_string(row)))}")
print(f"Answer part two: {len(tuple(row for row in rows if is_nice_string_bis(row)))}")

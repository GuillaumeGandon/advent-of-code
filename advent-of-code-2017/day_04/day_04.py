passphrases = tuple(row.split() for row in open("input").read().splitlines())

valid_passphrases = tuple(row for row in passphrases if len(row) == len(set(row)))
print(f"Answer part one: {len(valid_passphrases)}")

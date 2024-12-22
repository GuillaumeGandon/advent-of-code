from collections import defaultdict


def compute_next_secret(secret):
    secret ^= secret * 64
    secret %= 16777216
    secret ^= secret // 32
    secret %= 16777216
    secret ^= secret * 2048
    return secret % 16777216


part_1 = 0
sequences = defaultdict(lambda: 0)
for secret_number in map(int, open("input").read().splitlines()):
    secrets, changes = [secret_number % 10], []

    for i in range(2000):
        secret_number = compute_next_secret(secret_number)
        secrets.append(secret_number % 10)
        changes.append(secrets[i + 1] - secrets[i])
    part_1 += secret_number

    seen = set()
    for i in range(len(changes) - 3):
        seq = tuple(changes[i : i + 4])
        if seq not in seen:
            seen.add(seq)
            sequences[seq] += secrets[i + 4]


print(f"Answer part one: {part_1}")
print(f"Answer part two: {max(sequences.values())}")

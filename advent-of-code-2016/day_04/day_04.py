from collections import Counter


def get_five_most_common(letters):
    return "".join(
        c for c, _ in sorted(Counter(letters).items(), key=lambda x: (x[1], ord("z") - ord(x[0])), reverse=True)[:5]
    )


def rotate(letters, nb_rotation):
    return "".join(chr((ord(c) + nb_rotation - ord("a")) % (ord("z") - ord("a") + 1) + ord("a")) for c in letters)


rows = tuple(row.split("-") for row in open("input").read().splitlines())
encrypted_data = tuple(("".join(row[:-1]), int(row[-1][:3]), row[-1][4:9]) for row in rows)

sum_sector_ids = sum(
    sector_id for name, sector_id, checksum in encrypted_data if checksum == get_five_most_common(name)
)
print(f"Answer part one: {sum_sector_ids}")

decrypted_data = {rotate(name, sector_id): sector_id for name, sector_id, _checksum in encrypted_data}
print(f"Answer part two: {decrypted_data['northpoleobjectstorage']}")

def compute_replacements(molecule):
    return set(
        molecule[:i] + value + molecule[i + len(key):]
        for key, value in replacements
        for i in range(len(molecule) - len(key) + 1)
        if molecule[i:i + len(key)] == key
    )


def make_medicine(molecule, nb_steps=0):
    for v, k in replacements_sorted:
        if k in molecule:
            return make_medicine(molecule.replace(k, v), nb_steps + molecule.count(k))
    return nb_steps


rows = open('input').read().splitlines()
replacements = tuple(tuple(row.split(' => ')) for row in rows[:-2])
replacements_sorted = sorted(replacements, key=lambda x: len(x[1]) - len(x[0]), reverse=True)

medicine_molecule = rows[-1]

print(f"Answer part one: {len(compute_replacements(medicine_molecule))}")
print(f"Answer part two: {make_medicine(medicine_molecule)}")

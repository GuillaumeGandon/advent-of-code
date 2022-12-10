rows = open('input').read().splitlines()

nb_literal_characters = sum(len(row) for row in rows)
nb_memory_characters = sum(len(eval(f"str({row})")) for row in rows)
print(f"Answer part one: {nb_literal_characters - nb_memory_characters}")

nb_encoded_characters = sum(
    len(row.replace('\\', '\\\\').replace('"', '\\"')) + 2
    for row in rows
)
print(f"Answer part two: {nb_encoded_characters - nb_literal_characters}")

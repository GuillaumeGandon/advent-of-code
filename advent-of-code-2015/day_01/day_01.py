directions = open('input').read()

print(f"Answer part one: {sum(1 if d == '(' else -1 for d in directions)}")

floor = 0
for idx, d in enumerate(directions):
    if d == '(':
        floor += 1
    else:
        floor -= 1

    if floor == -1:
        print(f'Answer part two: {idx + 1}')
        break

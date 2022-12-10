MFCSAM = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0,
          'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}
GREATER = ('cats', 'trees')
FEWER = ('pomeranians', 'goldfish')

sues = []
for row in open('input').read().splitlines():
    sue_properties = {}
    for info in row.split(', '):
        if 'Sue' in info:
            name, value = info.split(': ')[1:]
        else:
            name, value = info.split(': ')
        sue_properties[name] = int(value)
    sues.append(sue_properties)

for idx, sue in enumerate(sues):
    if all(k not in sue or sue[k] == v for k, v in MFCSAM.items()):
        print(f"Answer part one: {idx + 1}")

    if all(
            k not in sue or
            k not in GREATER + FEWER and sue[k] == v or
            k in GREATER and sue[k] > v or
            k in FEWER and sue[k] < v
            for k, v in MFCSAM.items()
    ):
        print(f"Answer part two: {idx + 1}")

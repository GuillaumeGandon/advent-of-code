passwords_range = range(178416, 676461)

passwords_part_one = [
    i
    for i in passwords_range
    if (s := str(i)) == ''.join(sorted(s)) and any(1 for c in s if s.count(c) >= 2)
]
print(f'Answer part one: {len(passwords_part_one)}')

passwords_part_two = [
    i
    for i in passwords_range
    if (s := str(i)) == ''.join(sorted(s)) and any(1 for c in s if s.count(c) == 2)
]
print(f'Answer part two: {len(passwords_part_two)}')

changes = list(map(int, open("input").readlines()))
print(f"Answer part one: {sum(changes)}")

first_duplicate = False
frequency, frequencies = 0, {0}
while not first_duplicate:
    for change in changes:
        frequency += change
        if frequency in frequencies:
            print(f"Answer part two: {frequency}")
            first_duplicate = True
            break
        else:
            frequencies.add(frequency)

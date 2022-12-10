dots_input, folds_input = tuple(data.splitlines() for data in open("input").read().split("\n\n"))

dots = set((int(x), int(y)) for dot in dots_input for x, y in (dot.split(","),))
folds = tuple(tuple(fold.split()[-1].split("=")) for fold in folds_input)

part_one = True
for axe, value in folds:
    v = int(value)
    if axe == "x":
        dots = set((x, y) if x < v else (v - (x - v), y) for (x, y) in dots)
    else:
        dots = set((x, y) if y < v else (x, v - (y - v)) for (x, y) in dots)
    if part_one:
        print(f"Answer part one: {len(dots)}")
        part_one = False

print("Answer part two:")
for y in range(max(y for _, y in dots) + 1):
    part_two = ""
    for x in range(max(x for x, _ in dots) + 1):
        part_two += "#" if (x, y) in dots else " "
    print(part_two)

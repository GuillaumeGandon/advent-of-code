sections = tuple(
    tuple(tuple(map(int, elf.split("-"))) for elf in row.split(",")) for row in open("input").read().splitlines()
)


part_1 = sum(c <= a <= b <= d or a <= c <= d <= b for (a, b), (c, d) in sections)
part_2 = sum(c <= a <= d or c <= b <= d or a <= c <= b or a <= d <= b for (a, b), (c, d) in sections)


print(f"Answer part one: {part_1}")
print(f"Answer part two: {part_2}")

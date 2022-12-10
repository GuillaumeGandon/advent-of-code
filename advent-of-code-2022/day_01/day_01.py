calories = sorted((sum(map(int, elf.splitlines())) for elf in open("input").read().split("\n\n")), reverse=True)
print(f"Answer part one: {calories[0]}")
print(f"Answer part two: {sum(calories[:3])}")

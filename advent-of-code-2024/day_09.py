disk_map = list(map(int, open("input").read()))

raw_blocks = [[i // 2] * d if i % 2 == 0 else ["."] * d for i, d in enumerate(disk_map) if d != 0]
free_space = sum(len(b) for b in raw_blocks if b[0] == ".")
blocks = [x for b in raw_blocks for x in b]
sorted_blocks = sorted((b for b in blocks if b != "."), reverse=True)

compacted_blocks = blocks[: len(blocks) - free_space]
i = 0
for b in range(len(compacted_blocks)):
    if compacted_blocks[b] == ".":
        compacted_blocks[b] = sorted_blocks[i]
        i += 1

print(f"Answer part one: {sum(i * id for i, id in enumerate(compacted_blocks))}")


i = 0
while i < len(raw_blocks):
    idx = len(raw_blocks) - i - 1
    file = raw_blocks[idx]
    if file[0] != ".":
        for j in range(len(raw_blocks)):
            if j < idx and raw_blocks[j][0] == "." and len(raw_blocks[j]) >= len(file):
                tmp = []
                tmp.append(file)
                raw_blocks[idx] = ["."] * len(file)
                if len(raw_blocks[j]) > len(file):
                    tmp.append(["."] * (len(raw_blocks[j]) - len(file)))
                raw_blocks = raw_blocks[:j] + tmp + raw_blocks[j + 1 :]
                break
    i += 1

blocks = [x for b in raw_blocks for x in b]

print(f"Answer part two: {sum(i * id for i, id in enumerate(blocks) if id != ".")}")

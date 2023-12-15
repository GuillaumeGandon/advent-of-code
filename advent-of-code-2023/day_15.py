from collections import defaultdict


def hash(s):
    ans = 0
    for c in s:
        ans += ord(c)
        ans *= 17
        ans %= 256
    return ans


init_sequence = open("input").read().split(",")

part_1 = sum(hash(step) for step in init_sequence)

boxes = defaultdict(list)
for step in init_sequence:
    label = step.split("-")[0].split("=")[0]
    id_box = hash(label)
    if "-" in step:
        boxes[id_box] = [(l, f) for l, f in boxes[id_box] if label != l]
    else:
        focal_length = int(step.split("=")[1])
        if any(label == l for l, _ in boxes[id_box]):
            boxes[id_box] = [(l, f if label != l else focal_length) for l, f in boxes[id_box]]
        else:
            boxes[id_box].append((label, focal_length))


part_2 = sum((id_box + 1) * (if_focal + 1) * f for id_box, b in boxes.items() for if_focal, (_, f) in enumerate(b))

print(f"Answer part one: {part_1}")
print(f"Answer part two: {part_2}")

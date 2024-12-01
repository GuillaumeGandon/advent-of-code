location_ids = [(int(line.split()[0]), int(line.split()[-1])) for line in open("input").read().splitlines()]

left_list = sorted(left for left, right in location_ids)
right_list = sorted(right for left, right in location_ids)

print(f"Answer part one: {sum(abs(left - right) for left, right in zip(left_list, right_list))}")
print(f"Answer part two: {sum(left * right_list.count(left) for left, right in location_ids)}")

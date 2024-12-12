from collections import deque, defaultdict


def find_regions():
    regions = []
    for k, v in data.items():
        if any(k in r for r in regions):
            continue
        region = {k}
        queue = deque([k])
        while queue:
            pos = queue.popleft()
            for m in (1, -1, 1j, -1j):
                if pos + m in data and data[pos + m] == v and pos + m not in region:
                    queue.append(pos + m)
                    region.add(pos + m)
        regions.append(region)
    return regions


def find_region_perimeter(region):
    v = region.pop()
    region.add(v)
    v = data[v]
    return sum(pos + m not in data or data[pos + m] != v for pos in region for m in (1, -1, 1j, -1j))


def find_region_side_number(region):
    v = region.pop()
    region.add(v)
    v = data[v]
    perimeter = defaultdict(set)
    for pos in region:
        for m in (1, -1, 1j, -1j):
            if pos + m not in data or data[pos + m] != v:
                perimeter[m].add(pos + m)

    sides = 0
    for _, perimeter_part in perimeter.items():
        seen = set()
        for p in perimeter_part:
            if p not in seen:
                sides += 1
                queue = deque([p])
                while queue:
                    pos = queue.popleft()
                    if pos in seen:
                        continue
                    seen.add(pos)
                    for m in (1, -1, 1j, -1j):
                        if pos + m in perimeter_part:
                            queue.append(pos + m)

    return sides


data = {(x + y * 1j): v for y, line in enumerate(open("input").read().splitlines()) for x, v in enumerate(line)}

regions = find_regions()

print(f"Answer part one: {sum(len(r) * find_region_perimeter(r) for r in regions)}")
print(f"Answer part two: {sum(len(r) * find_region_side_number(r) for r in regions)}")

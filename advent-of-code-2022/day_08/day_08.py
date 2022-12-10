data = tuple(tuple(map(int, row)) for row in open("input").read().splitlines())
data_transposed = tuple(map(tuple, zip(*data)))


def visible_trees(trees):
    res = set()
    max_tree = -1
    for i, tree in enumerate(trees):
        if tree > max_tree:
            res.add(i)
            max_tree = tree
    return res


x_visible_trees = set()
for y in range(len(data)):
    for i in visible_trees(data[y]):
        x_visible_trees.add((y, i))
    for i in visible_trees(reversed(data[y])):
        x_visible_trees.add((y, len(data[y]) - 1 - i))


y_visible_trees = set()
for x in range(len(data_transposed)):
    for i in visible_trees(data_transposed[x]):
        y_visible_trees.add((i, x))
    for i in visible_trees(reversed(data_transposed[x])):
        y_visible_trees.add((len(data_transposed[x]) - 1 - i, x))


def viewing_distance(x, y, trees):
    current_tree = data[y][x]
    res = 0
    for tree in trees:
        res += 1
        if tree >= current_tree:
            return res
    return res


def scenic_score(x, y):
    return (
        viewing_distance(x, y, reversed(data[y][:x]))
        * viewing_distance(x, y, data[y][x + 1 :])
        * viewing_distance(x, y, reversed(data_transposed[x][:y]))
        * viewing_distance(x, y, data_transposed[x][y + 1 :])
    )


print(f"Answer part one: {len(x_visible_trees.union(y_visible_trees))}")
print(f"Answer part two: {max(scenic_score(x,y) for y in range(len(data)) for x in range(len(data[y])))}")

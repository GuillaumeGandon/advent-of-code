def count_possible_triangles(triangles):
    return sum(1 for t in triangles if sum(sorted(t)[:2]) > max(t))


row_triangles = tuple(tuple(map(int, row.split())) for row in open("input").read().splitlines())

column_triangles = tuple(
    tuple(row_triangles[j * 3 + k][i] for k in range(3)) for i in range(3) for j in range(len(row_triangles) // 3)
)

print(f"Answer part one: {count_possible_triangles(row_triangles)}")
print(f"Answer part two: {count_possible_triangles(column_triangles)}")

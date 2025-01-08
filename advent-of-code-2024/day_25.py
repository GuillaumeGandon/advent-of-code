keys_and_locks = [key.splitlines() for key in open("input").read().split("\n\n")]

keys = [x for x in keys_and_locks if x[0] == "....." and x[-1] == "#####"]
locks = [x for x in keys_and_locks if x[-1] == "....." and x[0] == "#####"]

locks_heights = [["".join(l[r][c] for r in range(len(l))).count("#") - 1 for c in range(len(l[0]))] for l in locks]
keys_heights = [["".join(l[r][c] for r in range(len(l))).count("#") - 1 for c in range(len(l[0]))] for l in keys]

print(sum(all(l + k <= 5 for l, k in zip(lock, key)) for lock in locks_heights for key in keys_heights))

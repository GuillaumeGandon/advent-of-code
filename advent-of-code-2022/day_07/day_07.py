from collections import defaultdict

commands = tuple(tuple(command.strip().splitlines()) for command in open("input").read().split("$") if command)

filesystem = defaultdict(dict)

current_dir = "/"
for command in commands:
    if "cd" in command[0]:
        path = command[0].split()[1]
        if path == "/":
            current_dir = "/"
        elif path == "..":
            current_dir = "/".join(current_dir.split("/")[:-1])
            if current_dir == "":
                current_dir = "/"
        else:
            if current_dir == "/":
                current_dir = f"{current_dir}{path}"
            else:
                current_dir = f"{current_dir}/{path}"
    elif "ls" in command[0]:
        for x, y in (row.split() for row in command[1:]):
            if x != "dir":
                filesystem[current_dir][y] = int(x)


dir_sizes = {k: sum(v.values()) for k, v in filesystem.items()}


def find_cum_size(key):
    return sum(v for k, v in dir_sizes.items() if k.startswith(f"{key}"))


dir_cum_sizes = {k: find_cum_size(k) for k in dir_sizes}


used_space = dir_cum_sizes["/"]
unused_space = 70000000 - used_space
need_to_free = 30000000 - unused_space


print(f"Answer part one: {sum(size for size in dir_cum_sizes.values() if size < 100000)}")
print(f"Answer part two: {min(size for size in dir_cum_sizes.values() if size > need_to_free)}")

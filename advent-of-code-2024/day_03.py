import re


def mul(m):
    x, y = list(map(int, m.replace("mul(", "").replace(")", "").split(",")))
    return x * y


data = open("input").read()
enabled_data = "".join(enabled.split("don't()")[0] for enabled in data.split("do()"))

pattern = r"mul\(\d+,\d+\)"

print(f"Answer part one: {sum(mul(m) for m in re.findall(pattern, data))}")
print(f"Answer part two: {sum(mul(m) for m in re.findall(pattern, enabled_data))}")

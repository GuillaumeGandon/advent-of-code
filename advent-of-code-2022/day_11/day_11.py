from copy import deepcopy
from math import prod

initial_monkeys = {
    int((monkey_row := monkey_data.splitlines())[0][7]): {
        "items": list(map(int, monkey_row[1].split(":")[1].strip().split(", "))),
        "operation": monkey_row[2].split("=")[1].strip(),
        "test": int(monkey_row[3].split("by")[1].strip()),
        True: int(monkey_row[4].split(":")[1].strip()[-1]),
        False: int(monkey_row[5].split(":")[1].strip()[-1]),
        "inspected": 0,
    }
    for monkey_data in open("input").read().split("\n\n")
}

primary_product = prod(v["test"] for v in initial_monkeys.values())


def solve(nb_rounds, manage_worry_levels):
    monkeys = deepcopy(initial_monkeys)
    for i in range(nb_rounds):
        for monkey_id in monkeys:
            for old in monkeys[monkey_id]["items"]:
                new = manage_worry_levels(eval(monkeys[monkey_id]["operation"]))
                new_monkey = monkeys[monkey_id][new % monkeys[monkey_id]["test"] == 0]
                monkeys[new_monkey]["items"].append(new)
            monkeys[monkey_id]["inspected"] += len(monkeys[monkey_id]["items"])
            monkeys[monkey_id]["items"] = []
    return prod(sorted([v["inspected"] for v in monkeys.values()], reverse=True)[:2])


print(f"Answer part one: {solve(20, lambda x: x // 3)}")
print(f"Answer part two: {solve(10000, lambda x: x % primary_product)}")

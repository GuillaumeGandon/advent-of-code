data = open("input").read().strip()


def solve(message_length):
    for i in range(len(data) - message_length + 1):
        if len(set(data[i : i + message_length])) == message_length:
            return i + message_length


print(f"Answer part one: {solve(message_length=4)}")
print(f"Answer part two: {solve(message_length=14)}")

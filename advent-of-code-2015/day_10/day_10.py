from functools import cache


@cache
def look_and_say(value):
    count = 0
    cc = value[0]
    res = ''
    for c in value:
        if c == cc:
            count += 1
        else:
            res += f"{count}{cc}"
            count = 1
            cc = c

    return res + f"{count}{cc}"


def look_and_say_n_times(value, n):
    for _ in range(n):
        value = look_and_say(value)
    return value


input = '1113222113'

print(f"Answer part one: {len(look_and_say_n_times(input, 40))}")
print(f"Answer part two: {len(look_and_say_n_times(input, 50))}")

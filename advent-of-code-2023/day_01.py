def calibration(data):
    only_digits = ("".join(c for c in line if c.isdigit()) for line in data)
    return sum(int("".join([line[0], line[-1]])) for line in only_digits if line)


def replace_spelled_digit(data):
    return (
        line.replace("one", "one1one")
        .replace("two", "two2two")
        .replace("three", "three3three")
        .replace("four", "four4four")
        .replace("five", "five5five")
        .replace("six", "six6six")
        .replace("seven", "seven7seven")
        .replace("eight", "eight8eight")
        .replace("nine", "nine9nine")
        for line in data
    )


data = open("input").read().splitlines()

print(f"Answer part one: {calibration(data)}")
print(f"Answer part two: {calibration(replace_spelled_digit(data))}")

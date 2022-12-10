input = open("input").read().splitlines()


gamma_rate = "".join("0" if col.count("0") > col.count("1") else "1" for col in map(list, zip(*input)))
epsilon_rate = "".join("0" if char == "1" else "1" for char in gamma_rate)


power_consumption = int(gamma_rate, 2) * int(epsilon_rate, 2)
print(f"Answer part one: {power_consumption}")


def find_rating_value(most_common):
    a, b = "1", "0"
    if most_common:
        a, b = "0", "1"

    numbers = input
    for i in range(len(numbers)):
        transpose = list(map(list, zip(*numbers)))
        if transpose[i].count("0") > transpose[i].count("1"):
            numbers = [line for line in numbers if line[i] == a]
        else:
            numbers = [line for line in numbers if line[i] == b]

        if len(numbers) == 1:
            return int(numbers[0], 2)


oxygen_generator_rating = find_rating_value(most_common=True)
co2_scrubber_rating = find_rating_value(most_common=False)

life_support_rating = oxygen_generator_rating * co2_scrubber_rating
print(f"Answer part two: {life_support_rating}")

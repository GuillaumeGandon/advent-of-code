school = [0] * 9
for time in map(int, open("input").read().split(",")):
    school[time] += 1


def compute(nb_days):
    for _ in range(nb_days):
        fish = school.pop(0)
        school[6] += fish
        school.append(fish)
    return sum(school)


print(f"Answer part one: {compute(nb_days=80)}")
print(f"Answer part two: {compute(nb_days=256-80)}")

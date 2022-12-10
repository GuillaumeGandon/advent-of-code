tower = {}
for disc in open("input").read().splitlines():
    if "->" in disc:
        program, subs = disc.split(" -> ")
        name, weight = program.split(" ")
        weight = int(weight.replace("(", "").replace(")", ""))
        tower[name] = {"subs": tuple(subs.split(", ")), "weight": weight}
    else:
        name, weight = disc.split(" ")
        weight = int(weight.replace("(", "").replace(")", ""))
        tower[name] = {"weight": weight}


bottom_program = tuple(disc for disc in tower if not any(disc in meta.get("subs", []) for meta in tower.values()))[0]
print(f"Answer part one: {bottom_program}")


def get_weight(disc_name):
    disc = tower[disc_name]
    if "subs" in disc:
        subs_weigth = tuple(get_weight(sub) for sub in disc["subs"])
        first = subs_weigth[0]
        if any(first != weight for weight in subs_weigth):
            wrong_name, wrong_weight = tuple(
                (name, weight) for name, weight in zip(disc["subs"], subs_weigth) if subs_weigth.count(weight) == 1
            )[0]
            good_weight = tuple(weight for weight in subs_weigth if subs_weigth.count(weight) != 1)[0]
            print(tower[wrong_name]["weight"] - wrong_weight + good_weight)
        return disc["weight"] + sum(subs_weigth)
    else:
        return disc["weight"]


get_weight(bottom_program)

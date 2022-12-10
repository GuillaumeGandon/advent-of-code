from itertools import combinations

# ITEM: (Cost, Damage, Armor)
WEAPONS = {
    'Dagger': (8, 4, 0),
    'Shortsword': (10, 5, 0),
    'Warhammer': (25, 6, 0),
    'Longsword': (40, 7, 0),
    'Greataxe': (74, 8, 0),
}

ARMORS = {
    'No armor': (0, 0, 0),
    'Leather': (13, 0, 1),
    'Chainmail': (31, 0, 2),
    'Splintmail': (53, 0, 3),
    'Bandedmail': (75, 0, 4),
    'Platemail': (102, 0, 5),
}

RINGS = {
    'Damage +1': (25, 1, 0),
    'Damage +2': (50, 2, 0),
    'Damage +3': (100, 3, 0),
    'Defense +1': (20, 0, 1),
    'Defense +2': (40, 0, 2),
    'Defense +3': (80, 0, 3),
}


def play_game(items):
    my_hp = MY_HP
    boss_hp, boss_damage, boss_armor = BOSS_STATS
    (my_damage, my_armor), gold_spend = do_shopping(items)
    while my_hp > 0:
        boss_hp -= 1 if boss_armor >= my_damage else my_damage - boss_armor
        if boss_hp <= 0:
            break
        my_hp -= 1 if my_armor >= boss_damage else boss_damage - my_armor

    return my_hp > 0, gold_spend


def do_shopping(items):
    weapon, armor, rings = items

    new_damage = WEAPONS[weapon][1]
    gold = WEAPONS[weapon][0]

    new_armor = ARMORS[armor][2]
    gold += ARMORS[armor][0]

    for ring in rings:
        gold += RINGS[ring][0]
        new_damage += RINGS[ring][1]
        new_armor += RINGS[ring][2]

    return (new_damage, new_armor), gold


BOSS_STATS = tuple(
    int(row.split(': ')[-1])
    for row in open('input').read().splitlines()
)

MY_HP = 100

all_items_possibilities = tuple(
    (weapon, armor, ring)
    for weapon in WEAPONS
    for armor in ARMORS
    for i in range(3)
    for ring in combinations(RINGS.keys(), i)
)

game_status = tuple(play_game(items) for items in all_items_possibilities)
print(f"Answer part one: {min(gold for win, gold in game_status if win)}")
print(f"Answer part two: {max(gold for win, gold in game_status if not win)}")

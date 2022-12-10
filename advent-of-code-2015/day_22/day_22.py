from random import choice

# Spells: (Cost, Damage, Armor, Life, Turns, Mana)
SPELLS = {
    'Magic Missile': (53, 4, 0, 0, 0, 0),
    'Drain': (73, 2, 0, 2, 0, 0),
    'Shield': (113, 0, 7, 0, 6, 0),
    'Poison': (173, 3, 0, 0, 6, 0),
    'Recharge': (229, 0, 0, 0, 5, 101),
}

SPELLS_WITH_EFFECT = ('Shield', 'Poison', 'Recharge')


def pick_spell(active_spells, mana):
    spells = list(set(SPELLS.keys()) - set(active_spells.keys()))
    spells = [spell for spell in spells if mana >= SPELLS[spell][0]]
    if not spells:
        return None
    return choice(spells)


def apply_effect(active_spells, boss_hp, my_mana):
    damage_effect, armor_effect, mana_effect = 0, 0, 0
    deactivate_spells = []
    for active_spell in active_spells:
        _cost, damage, armor, _life, _turns, mana = SPELLS[active_spell]
        damage_effect += damage
        armor_effect += armor
        mana_effect += mana
        active_spells[active_spell] -= 1
        if active_spells[active_spell] == 0:
            deactivate_spells.append(active_spell)
    for deactivate_spell in deactivate_spells:
        del active_spells[deactivate_spell]
    return boss_hp - damage_effect, armor_effect, my_mana + mana_effect


def play_game(hard_mode=False):
    my_hp, my_mana, my_armor = MY_HP, MY_MANA, MY_ARMOR
    boss_hp, boss_damage = BOSS_STATS
    active_spells = {}
    mana_spend = 0
    selected_spell = None

    while my_hp > 0:
        # PLayer turn
        if hard_mode:
            my_hp -= 1
            if my_hp <= 0:
                break
        if active_spells:
            boss_hp, my_armor, my_mana = apply_effect(active_spells, boss_hp, my_mana)

        selected_spell = pick_spell(active_spells, my_mana)
        if not selected_spell:
            break
        cost, damage, armor, life, turns, mana = SPELLS[selected_spell]
        my_mana -= cost
        mana_spend += cost
        if selected_spell in SPELLS_WITH_EFFECT:
            active_spells[selected_spell] = turns
        else:
            my_hp += life
            boss_hp -= damage

        if boss_hp <= 0:
            break

        # Boss turn
        if active_spells:
            boss_hp, my_armor, my_mana = apply_effect(active_spells, boss_hp, my_mana)
        if boss_hp <= 0:
            break
        my_hp -= 1 if my_armor >= boss_damage else boss_damage - my_armor

    return my_hp > 0 and selected_spell, mana_spend


BOSS_STATS = tuple(
    int(row.split(': ')[-1])
    for row in open('input').read().splitlines()
)

MY_HP = 50
MY_MANA = 500
MY_ARMOR = 0

game_status = set(play_game() for _ in range(100_000))
print(f"Answer part one: {min(mana for win, mana in game_status if win)}")

game_status = set(play_game(hard_mode=True) for _ in range(100_000))
print(f"Answer part two: {min(mana for win, mana in game_status if win)}")

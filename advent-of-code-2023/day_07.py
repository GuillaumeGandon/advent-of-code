from functools import cmp_to_key, cache
from collections import Counter
from itertools import product

cards_mapping_part_1 = {
    card: i for i, card in enumerate(("A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"))
}
cards_mapping_part_2 = {
    card: i for i, card in enumerate(("A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"))
}

other_cards = ("A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2")


@cache
def get_type(h):
    nb_unique_cards = len(set(h))
    cards_count = sorted(Counter(h).values())
    if nb_unique_cards == 1:
        return 7
    elif cards_count == [1, 4]:
        return 6
    elif cards_count == [2, 3]:
        return 5
    elif cards_count == [1, 1, 3]:
        return 4
    elif cards_count == [1, 2, 2]:
        return 3
    elif nb_unique_cards == 4:
        return 2
    elif nb_unique_cards == 5:
        return 1


def compare_hands_part_1(a, b):
    h1, _ = a
    h2, _ = b

    t1 = get_type(h1)
    t2 = get_type(h2)
    if t1 > t2:
        return 1
    elif t1 == t2:
        for c1, c2 in zip(h1, h2):
            if cards_mapping_part_1[c1] < cards_mapping_part_1[c2]:
                return 1
            elif cards_mapping_part_1[c1] > cards_mapping_part_1[c2]:
                return -1
    else:
        return -1


@cache
def find_best_hand(h):
    max_hand = "23456"
    for comb in product(other_cards, repeat=h.count("J")):
        tmp_h = h
        for card in comb:
            tmp_h = tmp_h.replace("J", card, 1)
        if compare_hands_part_1((tmp_h, 0), (max_hand, 0)) == 1:
            max_hand = tmp_h
    return max_hand


def compare_hands_part_2(a, b):
    h1, _ = a
    h2, _ = b

    if "J" in h1:
        t1 = get_type(find_best_hand(h1))
    else:
        t1 = get_type(h1)

    if "J" in h2:
        t2 = get_type(find_best_hand(h2))
    else:
        t2 = get_type(h2)

    if t1 > t2:
        return 1
    elif t1 == t2:
        for c1, c2 in zip(h1, h2):
            if cards_mapping_part_2[c1] < cards_mapping_part_2[c2]:
                return 1
            elif cards_mapping_part_2[c1] > cards_mapping_part_2[c2]:
                return -1
    else:
        return -1


cmp_hands_part_1 = cmp_to_key(compare_hands_part_1)
cmp_hands_part_2 = cmp_to_key(compare_hands_part_2)


hands = tuple(line.split() for line in open("input").read().splitlines())


part_1 = sum(int(bid) * (i + 1) for i, (_, bid) in enumerate(sorted(hands, key=cmp_hands_part_1)))
part_2 = sum(int(bid) * (i + 1) for i, (_, bid) in enumerate(sorted(hands, key=cmp_hands_part_2)))

print(f"Answer part one: {part_1}")
print(f"Answer part two: {part_2}")

from math import prod
from collections import defaultdict

PROPERTIES = ('capacity', 'durability', 'flavor', 'texture')


def compute_score(proportions):
    return prod(tuple(
        max(
            sum(proportions[idx] * ingredient[property]
                for idx, ingredient in enumerate(ingredients.values())),
            0
        )
        for property in PROPERTIES
    ))


def compute_calories(proportions):
    return sum(
        proportions[idx] * ingredient['calories']
        for idx, ingredient in enumerate(ingredients.values())
    )


ingredients = defaultdict(dict)
for row in open('input').read().splitlines():
    ingredient_name, properties = row.split(': ')
    for property in properties.split(', '):
        property_name, property_value = property.split()
        ingredients[ingredient_name][property_name] = int(property_value)

max_score = max_score_500_calories = 0
for a in range(101):
    for b in range(101 - a):
        for c in range(101 - a - b):
            d = 100 - a - b - c
            score = compute_score((a, b, c, d))
            if score > max_score:
                max_score = score
            if compute_calories((a, b, c, d)) == 500 and score > max_score_500_calories:
                max_score_500_calories = score

print(f"Answer part one: {max_score}")
print(f"Answer part two: {max_score_500_calories}")

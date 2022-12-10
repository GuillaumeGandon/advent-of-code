def compute_additional_fuel(fuel_mass):
    res = int(fuel_mass) // 3 - 2
    if res > 0:
        return res + compute_additional_fuel(res)
    return 0


fuel_values = tuple(
    int(mass) // 3 - 2
    for mass in open('input').read().splitlines()
)
print(f'Answer part one: {sum(fuel_values)}')

additional_fuels = tuple(
    compute_additional_fuel(fuel_value)
    for fuel_value in fuel_values
)
print(f'Answer part two: {sum(additional_fuels) + sum(fuel_values)}')

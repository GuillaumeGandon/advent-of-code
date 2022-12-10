from functools import reduce


def factors(n):
    step = 2 if n % 2 else 1
    return set(reduce(list.__add__,
                      ([i, n // i] for i in range(1, int(n ** 0.5) + 1, step) if n % i == 0)))


number = 0
while 1:
    number += 1
    if sum(factors(number)) * 10 >= 33100000:
        print(f"Answer part one: {number}")
        break

while 1:
    number += 1
    if sum(p for p in factors(number) if number / p <= 50) * 11 >= 33100000:
        print(f"Answer part two: {number}")
        break

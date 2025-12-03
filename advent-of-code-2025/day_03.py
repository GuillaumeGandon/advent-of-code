def find_max_joltage(bank, expo):
    digit = max(bank[: len(bank) - expo])
    if expo == 0:
        return digit

    return digit * 10**expo + find_max_joltage(bank[bank.index(digit) + 1 :], expo - 1)


banks = tuple(tuple(map(int, bank)) for bank in open("input").read().splitlines())

print(f"Answer part one: {sum(find_max_joltage(bank, expo=1) for bank in banks)}")
print(f"Answer part two: {sum(find_max_joltage(bank, expo=11) for bank in banks)}")

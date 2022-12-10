segment_to_number = {
    "abcefg": "0",
    "cf": "1",
    "acdeg": "2",
    "acdfg": "3",
    "bcdf": "4",
    "abdfg": "5",
    "abdefg": "6",
    "acf": "7",
    "abcdefg": "8",
    "abcdfg": "9",
}


def decode(key, code):
    one = tuple(k for k in key if len(k) == 2)[0]
    four = tuple(k for k in key if len(k) == 4)[0]
    seven = tuple(k for k in key if len(k) == 3)[0]
    eight = tuple(k for k in key if len(k) == 7)[0]

    three = tuple(k for k in key if len(k) == 5 and all(s in k for s in one))[0]
    six = tuple(k for k in key if len(k) == 6 and sum(s in k for s in one) == 1)[0]

    code_to_number = {}
    code_to_number["a"] = (set(seven) - set(one)).pop()
    code_to_number["b"] = (set(four) - set(three)).pop()
    code_to_number["d"] = (set(four) - set(one) - set(code_to_number["b"])).pop()
    code_to_number["c"] = (set(four) - set(six)).pop()
    code_to_number["f"] = (set(four) - set(code_to_number.values())).pop()
    code_to_number["g"] = (set(three) - set(code_to_number.values())).pop()
    code_to_number["e"] = (set(eight) - set(code_to_number.values())).pop()

    decode_segment = {v: k for k, v in code_to_number.items()}
    return int("".join(segment_to_number["".join(sorted(decode_segment[x] for x in c))] for c in code))


input = tuple(tuple(segments.split() for segments in line.split(" | ")) for line in open("input").read().splitlines())

print(f"Answer part one: {sum(1 for _, code in input for segment in code if len(segment) in (2,3,4,7))}")
print(f"Answer part two: {sum(decode(*line) for line in input)}")

def find_numbers(data, skip_red=False):
    if isinstance(data, list):
        return sum(find_numbers(element, skip_red) for element in data)
    elif isinstance(data, dict):
        if skip_red and 'red' in data.values():
            return 0
        return sum(find_numbers(value, skip_red) for value in data.values())
    elif isinstance(data, int):
        return data
    else:
        return 0


json_input = eval(open('input').read())
print(f"Answer part one: {find_numbers(json_input)}")
print(f"Answer part two: {find_numbers(json_input, skip_red=True)}")

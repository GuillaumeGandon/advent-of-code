def count_zero(array):
    return array.count('0')


def get_pixel_color(pixel_idx, layer_idx):
    pixel_value = layers[layer_idx][pixel_idx]
    if pixel_value != '2':
        return pixel_value
    else:
        return get_pixel_color(pixel_idx, layer_idx + 1)


img = tuple(open('input').read().strip())
layers = tuple(img[i * (25 * 6): (i + 1) * (25 * 6)] for i in range(len(img) // (25 * 6)))

fewest_zeros = min(layers, key=count_zero)
print(f"Answer part one: {fewest_zeros.count('1') * fewest_zeros.count('2')}")

message = ''.join(
    tuple(get_pixel_color(i, 0) for i in range(25 * 6))
).replace('0', ' ').replace('1', '#')
print(f'Answer part two:')
for i in range(6):
    print(message[i * 25:(i + 1) * 25])

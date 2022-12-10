import hashlib


def find_number(key, nb_zero):
    zeros = '0' * nb_zero
    i = 0
    while 1:
        hash = hashlib.md5(f'{key}{i}'.encode('utf-8')).hexdigest()
        if hash[:nb_zero] == zeros:
            return i
        i += 1


print(f"Answer part one: {find_number('ckczppom', 5)}")
print(f"Answer part two: {find_number('ckczppom', 6)}")

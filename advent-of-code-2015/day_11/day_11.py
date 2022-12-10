BANNED_LETTERS = 'iol'


def increment_string(value):
    if value[-1] == 'z':
        return increment_string(value[:-1]) + 'a'
    return value[:-1] + chr(ord(value[-1]) + 1)


def find_next_password(pwd):
    while 1:
        pwd = increment_string(pwd)
        if (
                any(ord(pwd[j]) + 2 == ord(pwd[j + 1]) + 1 == ord(pwd[j + 2]) for j in range(6)) and
                not any(letter in pwd for letter in BANNED_LETTERS) and
                len([
                    letter
                    for letter in set(pwd)
                    if any(letter == pwd[i] == pwd[i + 1] for i in range(7))
                ]) == 2
        ):
            return pwd


input = 'hepxcrrq'

answer_part_one = find_next_password(input)
print(f"Answer part one: {answer_part_one}")
print(f"Answer part two: {find_next_password(answer_part_one)}")

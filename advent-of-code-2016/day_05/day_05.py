import hashlib


def hack_password(part_two=False, nb_character=8):
    password = [""] * nb_character if part_two else ""
    i = 0
    for _ in range(nb_character):
        while 1:
            x = hashlib.md5(f"{DOOR_ID}{i}".encode("utf-8")).hexdigest()
            i += 1
            if x[0:5] == "00000":
                if part_two:
                    if x[5].isnumeric() and int(x[5]) < nb_character and password[int(x[5])] == "":
                        password[int(x[5])] = x[6]
                        break
                else:
                    password += x[5]
                    break

    return "".join(password) if part_two else password


DOOR_ID = "ffykfhsq"

print(f"Answer part one: {hack_password()}")
print(f"Answer part two: {hack_password(part_two=True)}")

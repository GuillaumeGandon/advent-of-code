from itertools import permutations


def split_row(row):
    tmp = row.split()
    sign = 1
    if tmp[2] == 'lose':
        sign = -1
    return (tmp[0], tmp[-1][:-1]), sign * int(tmp[3])


def compute_happiness(seat_arr):
    nb_attendees = len(attendees)
    return sum(
        happiness_rules[(key := (seat_arr[i], seat_arr[(i + 1) % nb_attendees]))] + happiness_rules[key[::-1]]
        for i in range(nb_attendees)
    )


happiness_rules = dict(split_row(row) for row in open('input').read().splitlines())
attendees = set(attendee for attendee_pair in happiness_rules for attendee in attendee_pair)

print(f"Answer part one: {max(compute_happiness(seat_arr) for seat_arr in permutations(attendees))}")

happiness_rules.update({
    ('Me', attendee)[::way]: 0
    for attendee in attendees
    for way in (1, -1)
})
attendees.add('Me')
print(f"Answer part two: {max(compute_happiness(seat_arr) for seat_arr in permutations(attendees))}")

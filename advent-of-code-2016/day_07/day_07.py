ips = open("input").read().splitlines()


def parse_ip(ip):
    outside_square_bracket = []
    within_square_bracket = []
    tmp = ""
    for c in ip:
        if c == "[":
            outside_square_bracket.append(tmp)
            tmp = ""
        elif c == "]":
            within_square_bracket.append(tmp)
            tmp = ""
        else:
            tmp += c
    outside_square_bracket.append(tmp)
    return outside_square_bracket, within_square_bracket


def is_abba(s):
    return any(s[i] == s[i + 3] and s[i + 1] == s[i + 2] and s[i] != s[i + 1] for i in range(len(s) - 3))


def support_tls(ip):
    outside_square_bracket, within_square_bracket = parse_ip(ip)
    return any(is_abba(x) for x in outside_square_bracket) and not any(is_abba(x) for x in within_square_bracket)


def get_abas(s):
    return set(s[i : i + 3] for i in range(len(s) - 2) if s[i] == s[i + 2] and s[i] != s[i + 1])


def get_babs(s):
    return set(s[i + 1] + s[i] + s[i + 1] for i in range(len(s) - 2) if s[i] == s[i + 2] and s[i] != s[i + 1])


def support_ssl(ip):
    outside_square_bracket, within_square_bracket = parse_ip(ip)
    abas = set.union(*[get_abas(x) for x in outside_square_bracket])
    babs = set.union(*[get_babs(x) for x in within_square_bracket])
    return len(set.intersection(abas, babs)) != 0


print(f"Answer part one: {sum(support_tls(ip) for ip in ips)}")
print(f"Answer part two: {sum(support_ssl(ip) for ip in ips)}")

captcha = tuple(map(int, open("input").read().strip()))
len_captcha = len(captcha)

answer_part_one = sum(captcha[i] for i in range(len_captcha) if captcha[i] == captcha[(i + 1) % len_captcha])
print(f"Answer part one: {answer_part_one}")

answer_part_two = sum(
    captcha[i] for i in range(len_captcha) if captcha[i] == captcha[(i + len_captcha // 2) % len_captcha]
)
print(f"Answer part two: {answer_part_two}")

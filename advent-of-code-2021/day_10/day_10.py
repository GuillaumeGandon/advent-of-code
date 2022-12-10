from collections import deque

OPEN_CHARACTER = ("(", "[", "{", "<")
CLOSE_TO_OPEN = {")": "(", "]": "[", "}": "{", ">": "<"}
CHARACTER_TO_POINTS = {")": 3, "]": 57, "}": 1197, ">": 25137}


def split_corrupted_and_incomplete(line):
    queue = deque()
    for char in line:
        if char in OPEN_CHARACTER:
            queue.appendleft(char)
        else:
            if queue.popleft() != CLOSE_TO_OPEN[char]:
                return True, char
    return False, queue


def autocomplete_score(closing_sequence):
    score = 0
    CHARACTER_TO_POINTS = {"(": 1, "[": 2, "{": 3, "<": 4}
    for c in closing_sequence:
        score = score * 5 + CHARACTER_TO_POINTS[c]
    return score


corrupted_and_incomplete_lines = tuple(map(split_corrupted_and_incomplete, open("input").read().splitlines()))

illegal_characters = (char for is_corrupted, char in corrupted_and_incomplete_lines if is_corrupted)
closing_sequences = (queue for is_corrupted, queue in corrupted_and_incomplete_lines if not is_corrupted)

print(f"Answer part one: {sum(CHARACTER_TO_POINTS[c] for c in illegal_characters)}")

autocomplete_scores = sorted(map(autocomplete_score, closing_sequences))
print(f"Answer part two: {autocomplete_scores[len(autocomplete_scores) // 2]}")

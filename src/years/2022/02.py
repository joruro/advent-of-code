import sys
import os
sys.path.insert(0, os.path.abspath("src"))
from utils.api import get_input  # noqa: E402

input = get_input(2022, 2)


def calculate_score_part_one(matches):
    translation = {
        'X': 'A',
        'Y': 'B',
        'Z': 'C'
    }

    rules = {
        'A': 'C',
        'B': 'A',
        'C': 'B'
    }

    scores = {
        'A': 1,
        'B': 2,
        'C': 3
    }

    s = 0
    for m in matches:
        m = m.strip()
        m = m.split(" ")

        # Translate dict
        h = translation[m[1]]
        a = m[0]

        s += scores[h]

        # Draw
        if h == a:
            s += 3
        # Check if my action outscore opponent
        elif rules[h] == a:
            s += 6
        else:
            s += 0

    return s


def calculate_score_part_two(matches):
    rules_to_loose = {
        'A': 'C',
        'B': 'A',
        'C': 'B'
    }

    rules_to_win = {v: k for k, v in rules_to_loose.items()}

    scores = {
        'A': 1,
        'B': 2,
        'C': 3
    }

    s = 0
    for m in matches:
        m = m.strip()
        m = m.split(" ")

        # Translate dict
        a = m[0]

        # To loose
        if m[1] == 'X':
            h = rules_to_loose[a]
        # To draw
        elif m[1] == 'Y':
            s += 3
            h = a
        else:
            h = rules_to_win[a]
            s += 6

        s += scores[h]

    return s


part_one = calculate_score_part_one(input.split('\n'))
part_two = calculate_score_part_two(input.split('\n'))
print(part_one)
print(part_two)

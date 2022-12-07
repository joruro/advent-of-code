import sys
import os
sys.path.insert(0, os.path.abspath("src"))
from utils.api import get_input  # noqa: E402

input = get_input(2022, 1)


def get_most_calories(calories_set, top=3):
    total, current = [], 0
    for calories in calories_set:
        if calories == "":
            total.append(current)
            current = 0
        else:
            current += int(calories)
    total = sorted(total)
    return sum(total[-top:])


part_one = get_most_calories(input.split('\n'), 1)
part_two = get_most_calories(input.split('\n'), 3)
print(part_one)
print(part_two)

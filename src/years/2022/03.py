import sys
import os
sys.path.insert(0, os.path.abspath("src"))
from utils.api import get_input  # noqa: E402

input = get_input(2022, 3)

def get_priority(char):
    char = ord(char)

    if char >= 65 and char <= 90:
        return char - ord('A') + 27
    else:
        return char - ord('a') + 1


def sum_priorities_part_one(rucksacks):
    p = 0

    for r in rucksacks:
        r = r.strip()
        part_length = len(r) // 2
        left = r[:part_length]
        right = r[part_length:]

        left_items = {}
        right_items = {}

        for i in range(len(left)):
            left_items[left[i]] = True
            right_items[right[i]] = True

            if left[i] in right_items:
                p += get_priority(left[i])
                break

            if right[i] in left_items:
                p += get_priority(right[i])
                break

    return p


def sum_priorities_part_two(rucksacks):
    p = 0
    i = 0
    m = {}
    for r in rucksacks:
        r = r.strip()

        if i > 2:
            i = 0
            m = {}

        for c in r:
            m_i = m.get(c, {})
            m_i[i] = True
            m[c] = m_i
            if len(m_i) == 3:
                p += get_priority(c)
                break
        i += 1
    return p


part_one = sum_priorities_part_one(input.split('\n'))
part_two = sum_priorities_part_two(input.split('\n'))
print(part_one)
print(part_two)

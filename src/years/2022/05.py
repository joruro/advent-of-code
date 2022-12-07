import sys
import re
import os
sys.path.insert(0, os.path.abspath("src"))
from utils.api import get_input  # noqa: E402

input = get_input(2022, 5)


def build_stacks(stacks_input):
    stacks = None
    actions = []
    i = 0
    while stacks_input[i+1] != '':
        if not stacks:
            stacks = [[] for _ in range((len(stacks_input[i]) + 1) // 4)]
        actions.append(stacks_input[i])
        i += 1

    while actions:
        action = actions.pop()
        for i in range(0, len(action), 4):
            if action[i] == '[':
                stacks[i // 4].append(action[i+1])

    return stacks


def top_crates_part_one(moves, stacks):
    i = 0
    while not moves[i].startswith('move'):
        i += 1

    while i < len(moves) and moves[i].startswith('move'):
        result = re.search(r"move\s(\d+)\sfrom\s(\d+)\sto\s(\d+)", moves[i])
        (total, old_stack, new_stack) = result.groups()
        for _ in range(int(total)):
            stacks[int(new_stack) - 1].append(stacks[int(old_stack) - 1].pop())
        i += 1

    output = ''
    for stack in stacks:
        output += stack[-1]

    return output


def top_crates_part_two(moves, stacks):
    i = 0
    while not moves[i].startswith('move'):
        i += 1

    while i < len(moves) and moves[i].startswith('move'):
        result = re.search(r"move\s(\d+)\sfrom\s(\d+)\sto\s(\d+)", moves[i])
        (total, old_stack, new_stack) = result.groups()
        stacks[int(new_stack) - 1] += stacks[int(old_stack) - 1][-int(total):]
        for _ in range(int(total)):
            stacks[int(old_stack) - 1].pop()
        i += 1

    output = ''
    for stack in stacks:
        output += stack[-1]

    return output


lines = input.split('\n')
part_one = top_crates_part_one(lines, build_stacks(lines))
part_two = top_crates_part_two(lines, build_stacks(lines))
print(part_one)
print(part_two)
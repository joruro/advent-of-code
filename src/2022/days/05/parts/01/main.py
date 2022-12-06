import re
from '../../../../utils' import read_file_lines


def build_stacks(input):
    stacks = None
    actions = []
    i = 0
    while input[i+1] != '\n':
        input[i] = input[i].strip('\n')
        if not stacks:
            stacks = [[] for _ in range((len(input[i]) + 1) // 4)]
        actions.append(input[i])
        i += 1

    while actions:
        action = actions.pop()
        for i in range(0, len(action), 4):
            if action[i] == '[':
                stacks[i // 4].append(action[i+1])

    return stacks


def top_crates(moves, stacks):
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


f = open('2022/days/05/parts/01/input.txt', 'r')


lines = read_file_lines f.readlines()
stacks = build_stacks(lines)
r = top_crates(lines, stacks)

print(r)

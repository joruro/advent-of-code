import sys
import os
import math
sys.path.insert(0, os.path.abspath("src"))
from utils.api import get_input  # noqa: E402

input = get_input(2022, 9)


def count_unique_positions(moves, rope_size=10):
    rope = [(0, 0)] * rope_size
    positions = dict()
    for move in moves:
        direction, steps = move.split(' ')
        steps = int(steps)

        for _ in range(steps):
            positions[rope[0]] = True

            # Right
            if direction == 'R':
                rope[-1] = (rope[-1][0], rope[-1][1] + 1)
            # Left
            if direction == 'L':
                rope[-1] = (rope[-1][0], rope[-1][1] - 1)
            # Up
            if direction == 'U':
                rope[-1] = (rope[-1][0] + 1, rope[-1][1])
            # Down
            if direction == 'D':
                rope[-1] = (rope[-1][0] - 1, rope[-1][1])

            i = len(rope) - 1
            while i > 0:
                # Calculate distance
                if math.hypot(rope[i][0] - rope[i-1][0], rope[i][1] - rope[i-1][1]) >= 2:
                    # Calculate angle
                    angle = int(math.degrees(math.atan2(
                        rope[i][0] - rope[i-1][0], rope[i][1] - rope[i-1][1])))

                    if angle == 0:
                        rope[i-1] = (rope[i-1][0], rope[i-1][1] + 1)
                    elif angle == 26 or angle == 63 or angle == 45:
                        rope[i-1] = (rope[i-1][0] + 1, rope[i-1][1] + 1)
                    elif angle == 90:
                        rope[i-1] = (rope[i-1][0] + 1, rope[i-1][1])
                    elif angle == 116 or angle == 153 or angle == 135:
                        rope[i-1] = (rope[i-1][0] + 1, rope[i-1][1] - 1)
                    elif angle == 180:
                        rope[i-1] = (rope[i-1][0], rope[i-1][1] - 1)
                    elif angle == -116 or angle == -153 or angle == -135:
                        rope[i-1] = (rope[i-1][0] - 1, rope[i-1][1] - 1)
                    elif angle == -90:
                        rope[i-1] = (rope[i-1][0] - 1, rope[i-1][1])
                    elif angle == -26 or angle == -63 or angle == -45:
                        rope[i-1] = (rope[i-1][0] - 1, rope[i-1][1]+1)
                i -= 1

    positions[rope[0]] = True
    return len(positions)


lines = input.split("\n")
part_one = count_unique_positions(lines, 2)
part_two = count_unique_positions(lines, 10)
print(part_one)
print(part_two)

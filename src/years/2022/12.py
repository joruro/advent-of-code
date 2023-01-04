from collections import deque
import sys
import os
sys.path.insert(0, os.path.abspath("src"))
from utils.api import get_input  # noqa: E402

input = get_input(2022, 12)

sys.setrecursionlimit(2000)


def build_grid(lines):
    grid = []
    all_starting_pos = []
    starting_pos, ending_pos = None, None
    for i in range(len(lines)):
        row = list(lines[i])
        for j in range(len(row)):
            if row[j] == 'S':
                starting_pos = (i, j)
                row[j] = 'a'
            elif row[j] == 'E':
                ending_pos = (i, j)
                row[j] = 'z'

            if row[j] == 'a':
                all_starting_pos.append((i, j))

            row[j] = ord(row[j])
        grid.append(row)

    return grid, starting_pos, ending_pos, all_starting_pos


def get_next_moves(move, steps):
    return [
        {"current_pos": move, "move": (
            move[0], move[1] - 1), "steps": steps},  # left
        {"current_pos": move, "move": (
            move[0], move[1] + 1), "steps": steps},  # right
        {"current_pos": move, "move": (
            move[0] - 1, move[1]), "steps": steps},  # up
        {"current_pos": move, "move": (
            move[0] + 1, move[1]), "steps": steps},  # down
    ]


def find_shortest_path_bfs(grid, all_starting_pos, ending_pos):
    record = dict()

    next_moves = []
    for starting_pos in all_starting_pos:
        next_moves += get_next_moves(starting_pos, 0)
        record[starting_pos] = 0
    moves = deque(next_moves)

    total_steps = sys.maxsize
    while moves:
        # print(moves)
        move = moves.popleft()
        steps = move["steps"]
        current_pos = move["current_pos"]
        move = move["move"]

        if current_pos == ending_pos:
            total_steps = min(total_steps, steps)
            continue

        if move[0] < 0 or move[0] >= len(grid) or move[1] < 0 or move[1] >= len(grid[0]):
            continue

        if (grid[move[0]][move[1]] - grid[current_pos[0]][current_pos[1]]) > 1:
            continue

        if move in record:
            if record[move] <= (steps + 1):
                # print("move is already in record and number of steps is lower",
                #       move, (steps + 1), record[move])
                continue
            # else:
            #     print("move is already in record but number of steps is not lower",
            #           move, steps, record[move])
        steps += 1
        record[move] = steps
        # print(move, steps)
        next_moves = get_next_moves(move, steps)
        for next_move in next_moves:
            moves.append(next_move)
        # print("HERE 2", len(moves))

    # print(moves)
    return total_steps


def find_shortest_path_dfs(grid, current_pos, ending_pos, record=dict(), steps=0):
    record[current_pos] = steps
    # print("CURRENT", current_pos, steps, len(record))

    if current_pos == ending_pos:
        return steps

    next_moves = [
        (current_pos[0], current_pos[1] - 1),  # left
        (current_pos[0], current_pos[1] + 1),  # right
        (current_pos[0] - 1, current_pos[1]),  # up
        (current_pos[0] + 1, current_pos[1]),  # down
    ]

    steps_moves = []
    for move in next_moves:
        if move[0] < 0 or move[0] >= len(grid) or move[1] < 0 or move[1] >= len(grid[0]):
            continue

        if not (grid[move[0]][move[1]] - grid[current_pos[0]][current_pos[1]]) in [0, 1]:
            continue

        if move in record and record[move] <= (steps + 1):
            # print("NEXT DROPPED", move, steps, len(record))
            continue
        # print("NEXT NOT DROPPED", move, steps, record[move] if move in record else 0, len(record))

        # print("diff", current_pos, move,
        #       (grid[move[0]][move[1]] - grid[current_pos[0]][current_pos[1]]))

        steps_move = find_shortest_path_dfs(
            grid, move, ending_pos, record, steps + 1)

        if steps_move:
            steps_moves.append(steps_move)

    if steps_moves:
        return min(steps_moves)
    return 0


lines = input.split("\n")
grid, starting_pos, ending_pos, all_starting_pos = build_grid(lines)
print(grid, starting_pos, ending_pos, all_starting_pos)
# part_one = find_shortest_path_dfs(grid, starting_pos, ending_pos)
part_one = find_shortest_path_bfs(grid, [starting_pos], ending_pos)
part_two = find_shortest_path_bfs(grid, all_starting_pos, ending_pos)
print(part_one)
print(part_two)

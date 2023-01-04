import sys
import os
import math
from collections import deque
sys.path.insert(0, os.path.abspath("src"))
from utils.api import get_input  # noqa: E402

input = get_input(2022, 11)


def get_monkey_business_part_one():
    monkeys = [
        {
            "items": deque([99, 67, 92, 61, 83, 64, 98]),
            "operation": lambda worry: math.floor((worry * 17) / 3),
            "test": lambda worry: 4 if worry % 3 == 0 else 2,
            "inspected": 0
        },
        {
            "items": deque([78, 74, 88, 89, 50]),
            "operation": lambda worry: math.floor((worry * 11) / 3),
            "test": lambda worry: 3 if worry % 5 == 0 else 5,
            "inspected": 0
        },
        {
            "items": deque([98, 91]),
            "operation": lambda worry: math.floor((worry + 4) / 3),
            "test": lambda worry: 6 if worry % 2 == 0 else 4,
            "inspected": 0
        },
        {
            "items": deque([59, 72, 94, 91, 79, 88, 94, 51]),
            "operation": lambda worry: math.floor((worry * worry) / 3),
            "test": lambda worry: 0 if worry % 13 == 0 else 5,
            "inspected": 0
        },
        {
            "items": deque([95, 72, 78]),
            "operation": lambda worry: math.floor((worry + 7) / 3),
            "test": lambda worry: 7 if worry % 11 == 0 else 6,
            "inspected": 0
        },
        {
            "items": deque([76]),
            "operation": lambda worry: math.floor((worry + 8) / 3),
            "test": lambda worry: 0 if worry % 17 == 0 else 2,
            "inspected": 0
        },
        {
            "items": deque([69, 60, 53, 89, 71, 88]),
            "operation": lambda worry: math.floor((worry + 5) / 3),
            "test": lambda worry: 7 if worry % 19 == 0 else 1,
            "inspected": 0
        },
        {
            "items": deque([72, 54, 63, 80]),
            "operation": lambda worry: math.floor((worry + 3) / 3),
            "test": lambda worry: 1 if worry % 7 == 0 else 3,
            "inspected": 0
        },
    ]
    i = 0
    while i < 20:
        for monkey_index in range(len(monkeys)):
            monkey = monkeys[monkey_index]
            while monkey["items"]:
                # print(monkey["items"])
                item = monkey["items"].popleft()
                # print(monkey["items"], monkey["operation"](item))

                # exit(1)
                worry = monkey["operation"](item)
                test = monkey["test"](worry)
                # print(monkey_index, item, worry, test)
                monkeys[test]["items"].append(worry)
                monkey["inspected"] += 1
        i += 1

    inspected = []
    for monkey in monkeys:
        print(monkey["inspected"], monkey["items"])
        inspected.append(monkey["inspected"])

    inspected = sorted(inspected)

    return inspected[-1] * inspected[-2]


def get_monkey_business_part_two():
    monkeys = [

        {
            "items": deque([99, 67, 92, 61, 83, 64, 98]),
            "operation": lambda worry: (worry * 17),
            "test": 3,
            "true": 4,
            "false": 2,
            "inspected": 0
        },
        {
            "items": deque([78, 74, 88, 89, 50]),
            "operation": lambda worry: (worry * 11),
            "test": 5,
            "true": 3,
            "false": 5,
            "inspected": 0
        },
        {
            "items": deque([98, 91]),
            "operation": lambda worry: (worry + 4),
            "test": 2,
            "true": 6,
            "false": 4,
            "inspected": 0
        },
        {
            "items": deque([59, 72, 94, 91, 79, 88, 94, 51]),
            "operation": lambda worry: (worry * worry),
            "test": 13,
            "true": 0,
            "false": 5,
            "inspected": 0
        },
        {
            "items": deque([95, 72, 78]),
            "operation": lambda worry: (worry + 7),
            "test": 11,
            "true": 7,
            "false": 6,
            "inspected": 0
        },
        {
            "items": deque([76]),
            "operation": lambda worry: (worry + 8),
            "test": 17,
            "true": 0,
            "false": 2,
            "inspected": 0
        },
        {
            "items": deque([69, 60, 53, 89, 71, 88]),
            "operation": lambda worry: (worry + 5),
            "test": 19,
            "true": 7,
            "false": 1,
            "inspected": 0
        },
        {
            "items": deque([72, 54, 63, 80]),
            "operation": lambda worry: (worry + 3),
            "test": 7,
            "true": 1,
            "false": 3,
            "inspected": 0
        },
    ]

    i = 0
    while i < 10000:
        # print(i)

        # for monkey_index in range(len(monkeys)):
        #     print(monkey_index, len(monkeys[monkey_index]["items"]))

        for monkey_index in range(len(monkeys)):
            monkey = monkeys[monkey_index]
            while monkey["items"]:
                # print(monkey["items"])
                item = monkey["items"].popleft()
                # print(monkey["items"], monkey["operation"](item))

                # exit(1)
                worry = monkey["operation"](item)
                test_result = worry % monkey["test"]

                worry_new = worry % 9699690
                worry_new % monkey["test"]

                # print(monkey_index, item, monkey["test"], worry, worry,
                #       worry_new, worry_new % monkey["test"] == worry % monkey["test"])
                monkeys[monkey["true"] if test_result ==
                        0 else monkey["false"]]["items"].append(worry_new)
                monkey["inspected"] += 1

        # if i == 0 or i == 19 or i == 99 or i == 999:
        #     for monkey_index in range(len(monkeys)):
        #         print(i+1, monkey_index, monkeys[monkey_index]
        #               ["inspected"], len(monkeys[monkey_index]["items"]))

        i += 1

    inspected = []
    for monkey in monkeys:
        # print(monkey["inspected"], monkey["items"])
        inspected.append(monkey["inspected"])

    inspected = sorted(inspected)

    return inspected[-1] * inspected[-2]


# part_one = get_monkey_business_part_one()
part_two = get_monkey_business_part_two()
# print(part_one)
print(part_two)

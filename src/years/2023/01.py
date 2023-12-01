import sys
import os
from collections import deque

sys.path.insert(0, os.path.abspath("src"))
from utils.api import get_input  # noqa: E402

input = get_input(2023, 1)

# WRITE YOUR SOLUTION HERE
numbers_map = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}


def get_number(str):
    if str in numbers_map:
        return numbers_map[str]
    return None


def get_first_and_last_digits(line):
    start, end = 0, len(line) - 1
    tens_str, ones_str = deque([]), deque([]) 
    tens_found, ones_found = False, False
    while not tens_found or not ones_found:
        if not tens_found:
            for i in range(2,6):
                number = get_number(line[start:start+i])
                # print(number, line[start:start+i], i)
                if number:
                    tens_found = True
                    tens = number
                    break

        if not tens_found and line[start].isnumeric():
            tens_found = True
            tens = line[start]

        if not ones_found:
            for i in range(2,6):
                number = get_number(line[end-i:end+1])
                # print(number, line[end-i:end+1], i)
                if number:
                    ones_found = True
                    ones = number
                    break

        if not ones_found and line[end].isnumeric():
            ones_found = True
            ones = line[end]
        

    #     print(tens_str,ones_str)
    #     if not tens_found:
    #         tens = line[start] 
        
    #     if not ones_found:
    #         ones = line[end]

    #     if tens.isnumeric():
    #         tens_found = True

    #     if ones.isnumeric():
    #         ones_found = True


    #     tens_str.append(tens)
    #     ones_str.append(ones)

    #     if not tens_found:
    #         if len(tens_str) >= 3 and len(tens_str) <= 5:
    #             number = get_number(''.join(tens_str))
    #             if number is not False:
    #                 tens_found = True
    #                 tens = number
            
    #         if len(tens_str) > 5:
    #             while len(tens_str) > 3:
    #                 tens_str.popleft()
    #                 number = get_number(''.join(tens_str))
    #                 if number is not False:
    #                     tens_found = True
    #                     tens = number
    #                     break
        
    #     if not ones_found:
    #         if len(ones_str) >= 3 and len(ones_str) <= 5:
    #             number = get_number(''.join(reversed(ones_str)))
    #             if number is not False:
    #                 ones_found = True
    #                 ones = number
            
    #         if len(ones_str) > 5:
    #             while len(ones_str) > 3:
    #                 ones_str.popleft()
    #                 number = get_number(''.join(reversed(ones_str)))
    #                 if number is not False:
    #                     ones_found = True
    #                     ones = number
    #                     break
            
        if not tens_found:
            start += 1
        if not ones_found:
            end -= 1
    
    print(int(tens + ones))

    return int(tens + ones)


def get_sum(input):
    sum = 0
    for i in input:
        sum += get_first_and_last_digits(i)
    return sum

print(get_sum(input.split('\n')))


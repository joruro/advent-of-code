import sys
import os
sys.path.insert(0, os.path.abspath("src"))
from utils.api import get_input  # noqa: E402
from collections import defaultdict

input = get_input(2023, 4)

# WRITE YOUR SOLUTION HERE

cards = [0] * 206
print(cards)

def process_cards(line, index):
    [numbers, winning] = line.split('|')

    winning =  winning.strip().split(' ')
    w_dict = defaultdict(bool)
    # print(winning)
    for w in winning:
        if w == '':
            continue
        w_dict[int(w.strip(' '))] = True
    
    # print(w_dict)
    
    numbers = numbers.split(':')[1]
    # print(numbers)
    numbers = numbers.strip().split(' ')
    # print(numbers)

    next = 1

    if cards[index] == 0:
        cards[index] = 1

    for n in numbers:
        if n == '':
            continue
        
        if w_dict[int(n)]:
            if cards[index+next] == 0:
                cards[index+next] = 1
            cards[index+next] += cards[index] * 1
            next +=1

    

def get_total_cards(input):
    i = 0
    for line in input:
        process_cards(line, i)
        i += 1
    print(cards, sum(cards))
    

print(get_total_cards(input.split('\n')))
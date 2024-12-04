import sys
import functools
import itertools
import re

data = open('input').read()
def part1():
    matches = re.findall('mul\([0-9]+,[0-9]+\)', data)
    pairs = [list(map(int, y)) for y in [re.findall('\d+', x) for x in matches]]
    result = sum([functools.reduce(lambda x, y : x * y, pair) for pair in pairs])

    return result

def part2():
    matches = re.findall('mul\([0-9]+,[0-9]+\)|don\'t\(\)|do\(\)', data)
    do_positions = []
    dont_positions = []

    for i in range(len(matches)):
        if matches[i] == "don't()":
            dont_positions.append(i)
        if matches[i] == 'do()':
            do_positions.append(i)

    pairs = [list(map(int, y)) for y in [re.findall('\d+', x) for x in matches]]
    values = [functools.reduce(lambda x,y : x*y, pair) if pair else [] for pair in pairs]
    
    acc = True
    result = 0

    for i in range(len(values)):
        if values[i] == []:
            if i in dont_positions:
                acc = False
            else:
                acc = True
            continue
        if acc:
            result += values[i]
    return result



print("The result of Part 1 is {}".format(part1()))
print("The result of Part 2 is {}".format(part2()))
import itertools
import functools


def check(target, numbers, part2 = False):
    n = len(numbers)
    add = lambda x,y : x+y
    mul = lambda x,y : x*y
    con = lambda x,y : int(str(x) + str(y))

    possibilites1 = [tuple(c) for c in itertools.product([mul, add], repeat=n-1)]
    possibilites2 = [tuple(c) for c in itertools.product([mul, con, add], repeat=n-1)]
    possibilites = possibilites2 if part2 else possibilites1
    
    for p in possibilites:
        result = numbers[0]
        for i in range(n-1):
            result = p[i](result, numbers[i+1])
        if result == target:
            return (True, result)
    return (False, None)

def solve(file, part2=False):
    result = 0
    data = [line.split(' ') for line in open(file).read().strip().split('\n')]
    for line in data:
        target = int(line[0][:-1])
        numbers = list(map(int, line[1:]))
        
        (valid, s) = check(target, numbers, True) if part2 else check(target, numbers, False)
        if valid:
            result += s
    
    return result

print(solve('input07', True))
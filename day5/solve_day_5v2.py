from functools import cmp_to_key

def cmp(a,b):
    return -1 if (a,b) in rules else 1 if (b,a) in rules else 0


data = open('input05').readlines()
rules = [tuple(line.strip().split('|')) for line in data if '|' in line]
updates = [line.strip().split(",") for line in data if ',' in line]

part1 = sum([int(update[len(update)//2]) for update in updates if sorted(update, key=cmp_to_key(cmp)) == update])
part2 = 0 
for update in updates:
    proper = sorted(update, key=cmp_to_key(cmp))
    if proper != update:
        part2 += int(proper[len(proper)//2])
print(part1, part2)
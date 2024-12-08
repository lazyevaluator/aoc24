import itertools

grid = [line.strip() for line in open('input08')]

n, m = len(grid), len(grid[0])
antennas = {}
unique_part1 = set()
unique_part2 = set()

def inGrid(position):
    r, c = position
    if r < 0 or c < 0 or r >= n or c >= m: 
        return False
    else:
        return True


for r, row in enumerate(grid):
    for c, char in enumerate(row):
        if not char == ".":
            if not char in antennas: antennas[char] = []
            antennas[char].append((r,c))

for positions in antennas.values():
    for ((r1, c1), (r2, c2)) in itertools.combinations(positions, 2):
        antinodes_part1 = [(2*r1 - r2, 2*c1 - c2), (2*r2 - r1, 2*c2 - c1)]

        # this will generate all antinodes but potentially also many points outside the grid
        antinodes_part2 = [(r1 - k*(r2-r1), c1 - k*(c2-c1)) for k in range(-max(n,m), max(n,m))]
        for a in antinodes_part1:
            if inGrid(a):
                unique_part1.add(a)

        for b in antinodes_part2:
            if inGrid(b):
                unique_part2.add(b)

print(len(unique_part1), len(unique_part2))
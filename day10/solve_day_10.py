grid = [[int(x) for x in row] for row in open('input10').read().strip().split('\n')]

def getNeighbors(pos, grid):
    n, m = len(grid), len(grid[0])
    i, j = pos
    delta = [(1,0), (-1,0), (0,1), (0, -1)]
    neighbors = [(i+dx, j+ dy, grid[i+dx][j+dy]) for (dx,dy) in delta if i+dx >= 0 and i+dx < n and j+dy >= 0 and j+dy < m]

    return neighbors

def explorePath(pos, grid, part2 = False):
    # explores path until 9 is
    reachable = set() if not part2 else []
    def explorer(pos, grid):
        neighbors = getNeighbors(pos, grid)
        i, j = pos
        value = grid[i][j]

        if value == 9:
            if part2:
                reachable.append((i,j))
            else:
                reachable.add((i,j))
        
        for ne in neighbors:
            x, y, v = ne
            if v == value + 1:
                explorer((x, y), grid)
    
    explorer(pos, grid)
    return reachable


def score(grid, part2 = False):
    n, m = len(grid), len(grid[0])
    score = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                score += len(explorePath((i,j), grid, part2))

    return score

print("Part 1 = {}".format(score(grid)))
print("Part 2 = {}".format(score(grid, True)))
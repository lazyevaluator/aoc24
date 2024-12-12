""" 
    make a graph of the grid where nodes are (i,j,value)
    and e = {(x,y,v), (x',y',v')} \in E iff v = v' and abs(x-x') + abs(y-y') == 1
    then find components vid dfs.
    For each u in component
    add to perimeter
        4 if deg(u) == 0
        3 if deg(u) == 1
        2 if deg(u) == 2
        1 if deg(u) == 3
        0 if deg(u) == 4
        -> perimeter += 4 - deg(u)
"""

# recycled from day 10
def getNeighbors(pos, grid):
    n, m = len(grid), len(grid[0])
    i, j = pos
    delta = [(1,0), (-1,0), (0,1), (0, -1)]
    neighbors = [(i+dx, j + dy, grid[i+dx][j+dy]) for (dx,dy) in delta if i+dx >= 0 and i+dx < n and j+dy >= 0 and j+dy < m]

    return neighbors

grid = [[x for x in row] for row in open('input12').read().strip().split('\n')]


def buildGraph(grid):
    n, m, graph = len(grid), len(grid[0]), dict()
    for i in range(n):
        for j in range(m):
            v = grid[i][j]
            neighbors = getNeighbors((i,j), grid)
            graph[(i,j,v)] = [(x, y, w) for (x, y, w) in neighbors if v == w and abs(x-i) + abs(j-y) == 1]

    return graph


def getComponents(graph):
    components = []
    visited = set()
    
    def getComponent(v, component):
        component.add(v)
        visited.add(v)
        for w in graph[v]:
            if w not in component:
                getComponent(w, component)

        return component

    for v in graph:
        if v not in visited:
            component = getComponent(v, component=set())
            components.append(component)
    return components


def price(graph):
    d = lambda v: len(graph[v])
    components = getComponents(graph)
    price = 0


    for c in components:
        area = 0
        perimeter = 0
        for v in c:
            area += 1
            perimeter += 4 - d(v)
        price += area*perimeter
    
    return price
            


graph = buildGraph(grid)

print(price(graph))
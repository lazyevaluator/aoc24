import sys


data = open('input06_tiny').read().strip().split('\n')

card = [[data[i][j] for j in range(len(data[i]))] for i in range(len(data))]

n = len(card)
m = len(card[0])
sys.setrecursionlimit((n*m)**2)

def find_start(card):
    for i in range(len(card)):
        for j in range(len(card[i])):
            if card[i][j] == '^':
                return (i,j)
            
def simulate_walk(card):
    distinct = 0
    up = (-1,0)
    down = (1, 0)
    left = (0, -1)
    right = (0, 1)
    directions = [up, right, down, left]
    visited = set()

    def walk(pos, direction, card):
        nonlocal distinct
        x, y = pos
        dx, dy = directions[direction]

        if pos not in visited:
            distinct += 1
        visited.add(pos)
        card_x_y = card[x][y]
        card[x][y] = direction


        if x + dx >= n or x + dx < 0 or y+dy >= m or y+dy < 0:
            # will leave the map
            return
        
        # part b
        if card[x+dx][y+dy] in visited and card[x+dx][y+dy] == direction:
            return -1

        if card[x+dx][y+dy] != '#':
            walk((x+dx, y+dy), direction, card)

        if card[x+dx][y+dy] == '#':
            new_direction = (direction + 1) % 4
            new_dx, new_dy = directions[new_direction]
            walk((x+new_dx, y+new_dy), new_direction, card)
        # restore
        card[x][y] = card_x_y
        

    walk(find_start(card), 0, card)
    return distinct

def part2(card):
    locations = 0
    start = find_start(card)
    for i in range(n):
        for j in range(m):
            if (i,j) == start:
                continue
            card_copy = card.copy()
            card_copy[i][j] = "#"
            if simulate_walk(card_copy) == -1:
                locations += 1
    return locations

card_copy1 = card.copy()
# print(simulate_walk(card_copy1))
print(part2(card_copy1))


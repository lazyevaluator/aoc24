# for every index tuple (i,j) in data check if there starts XMAS in forward directions
# then search with backward pattern in forward direction

def forward_count(puzzle, pattern):
    matches = 0
    n = len(puzzle)
    d = len(pattern)
    for i in range(n):
        for j in range(n):

            # horizontal check
            if (j + d -1 < n):
                subword = [puzzle[i][j + x] for x in range(d)]
                if subword == pattern:
                    matches += 1
            
            # vertical check
            if (i + d - 1 < n):
                subword = [puzzle[i + x][j] for x in range(d)]
                if subword == pattern:
                    matches += 1
            
            # diagonal check
            if (i + d - 1 < n and j + d - 1 < n):
                subword = [puzzle[i + x][j + x] for x in range(d)]
                if subword == pattern:
                    matches += 1
            if (i + d - 1 < n and j - d + 1 >= 0):
                subword = [puzzle[i + x][j - x] for x in range(d)]
                if subword == pattern:
                    matches += 1
    return matches


def cross_count(puzzle):
    crosses = 0
    n = len(puzzle)
    pattern1 = ['M', 'A', 'S']
    pattern2 = list(reversed(pattern1))
    d = len(pattern1)

    for i in range(n):
        for j in range(n):
            if (i + d-1 < n and j + d-1 < n):
                subword1 = [puzzle[i+x][j+x] for x in range(d)]
                subword2 = [puzzle[i+x][j+d-1-x] for x in range(d)]

                poss1 = subword1 == pattern1 and subword2 == pattern1 
                poss2 = subword1 == pattern1 and subword2 == pattern2
                poss3 = subword1 == pattern2 and subword2 == pattern1
                poss4 = subword1 == pattern2 and subword2 == pattern2

                match = poss1 or poss2 or poss3 or poss4
                if match:
                    crosses += 1
                    # print("i,j = {},{}".format(i,j))
    return crosses


puzzle1 = open('input04').read().split('\n')
puzzle2 = open('input04_tiny').read().split('\n')


forward_pattern = ['X', 'M', 'A', 'S']
backward_pattern = list(reversed(forward_pattern))
count = forward_count(puzzle=puzzle1, pattern=forward_pattern)
count += forward_count(puzzle=puzzle1, pattern=backward_pattern)
print(count)
print(cross_count(puzzle1))
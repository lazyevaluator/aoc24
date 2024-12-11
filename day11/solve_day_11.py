import functools

data = [int(x) for x in open('input11').read().strip().split()]

def blink(stones :list[int]):
    new_stones = []
    for i, stone in enumerate(stones):
        if stone == 0:
            new_stones.append(1)
        
        elif len(str(stone)) % 2 == 0:
            s = str(stone)
            d = len(s) // 2

            left = int(s[:d])
            right = int(s[d:])

            new_stones.append(left)
            new_stones.append(right)

        else:
            new_stones.append(stones[i] * 2024)
    return new_stones

# print(data)

def blink_n(n, stones):
    new_stones = stones
    for i in range(n):
        new_stones = blink(new_stones)
    return new_stones

print(len(blink_n(25, data)))   

# part 2
# let f(n,m) denote the number of stones after blinking m times starting with only the single stone n
# use memoization with dictionary where the keys are pairs (n,m)

"""
The recursive formula for f is 
f(n,m) = { 
           1                                      if m = 0
           l(1, m - 1)                            if n = 0
           l(left(n), m - 1) + l(right(n), m - 1) if n has even number of digits
           l(2024*n, m - 1)                       otherwise
         }
"""

def f(n,m):
    table = dict()
    def f_helper(n,m):
        if (n,m) in table:
            return table[(n,m)]

        if m == 0:
            table[(n,m)] = 1
        elif n == 0:
            table[(n,m)] = f_helper(1, m - 1)

        elif len(str(n)) % 2 == 0:
            s = str(n)
            d = len(s) // 2

            left = int(s[:d])
            right = int(s[d:])
            table[(n,m)] = f_helper(left, m - 1) + f_helper(right, m - 1)
        
        else:
            table[(n,m)] = f_helper(2024*n, m - 1)

        return table[(n,m)]
    
    return f_helper(n,m)

m = 75
stones = 0
for x in data:
    stones += f(x, m)
print(stones)
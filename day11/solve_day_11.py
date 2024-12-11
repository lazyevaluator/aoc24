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

print(len(blink_n(35, data)))    
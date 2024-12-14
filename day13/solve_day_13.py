import re

data = open('input13').read().strip().split('\n\n')
tokens = 0

for machine in data:
    numbers = [int(x) for x in re.findall(r'\d+', machine)]
    a, c, b, d = numbers[:4]
    y_1, y_2 = numbers[-2:]
    
    n = b*c - a*d
    z_1 = (-d*y_1 + b * y_2) 
    z_2 = (c*y_1 - a*y_2)

    if z_1 % n == 0 and z_2 % n == 0:
        x_1, x_2 = int(z_1 / n), int(z_2 / n)
        if max(x_1, x_2) <= 100:
            tokens += 3*x_1 + x_2

print(tokens)
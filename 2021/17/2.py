import re

def sign(a):
    return (a > 0) - (a < 0)

data = open('input').read()

x0, x1, y0, y1 = map(int, re.findall("target area: x=([-0-9]+)..([-0-9]+), y=([-0-9]+)..([-0-9]+)", data)[0])

def simulate(vx, vy):
    x, y = 0, 0
    while True:
        x += vx
        y += vy
        vx -= sign(vx)
        vy -= 1
        if x0 <= x <= x1 and y0 <= y <= y1:
            return True
        if y < y0:
            return False


total = 0
for vx in range(1, x1+1):
    for vy in range(y0, -y0+1):
        total += simulate(vx, vy)
print(total)
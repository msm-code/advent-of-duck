from enum import Flag
import re

data = open("input").read().strip()

MIN_XY = 200000000000000
MAX_XY = 400000000000000

hail = re.findall("(-?\\d+), +(-?\\d+), +(-?\\d+) @ +(-?\\d+), +(-?\\d+), +(-?\\d+)", data)
hail = [tuple(int(e) for e in h) for h in hail]

def withx0(x, y, vx, vy):
    v = vy / vx
    return y - x * v

def collide(h0, h1):
    if h0[3:] == h1[3:]:
        assert False
    x0, y0, z0, vx0, vy0, vz0 = h0
    x1, y1, z1, vx1, vy1, vz1 = h1
    h0, h1 = withx0(x0, y0, vx0, vy0), withx0(x1, y1, vx1, vy1)
    dy = (vy0 / vx0) - (vy1 / vx1)
    if dy == 0: return None
    tx = (h1 - h0) / dy
    ty = h0 + (vy0 / vx0) * tx
    t0, t1 = (tx - x0) / vx0, (tx - x1) / vx1
    if t0 < 0 or t1 < 0: return None
    if tx < MIN_XY or ty < MIN_XY or tx > MAX_XY or ty > MAX_XY: return None
    return (tx, ty)


colls = 0
for i, h0 in enumerate(hail):
    for j, h1 in enumerate(hail[i+1:]):
        if collide(h0, h1) is not None: colls += 1
print(colls)

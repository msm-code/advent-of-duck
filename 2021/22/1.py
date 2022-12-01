import re

point="([-0-9]+)..([-0-9]+)"
commands = re.findall(f"(.*) x={point},y={point},z={point}", open('input').read())
commands = [[c[0]] + list(int(v) for v in c[1:]) for c in commands]
commands = [cmd for cmd in commands if all(-50 <= c <= 50 for c in cmd[1:])]
commands = [(int(c == "on"), (x0, x1+1), (y0, y1+1), (z0, z1+1)) for c, x0, x1, y0, y1, z0, z1 in commands]

xs, ys, zs = [sorted(set([v for c in commands for v in c[i]])) for i in [1, 2, 3]]
zstep = (len(zs) - 1)
ystep = (len(ys) - 1) * zstep
rsize = (len(xs) - 1) * ystep
reactor = [0] * rsize

for (c, (x0, x1), (y0, y1), (z0, z1)) in commands:
    for xi, (X0, X1) in enumerate(zip(xs, xs[1:])):
        if not (x0 <= X0 and X1 <= x1): continue
        for yi, (Y0, Y1) in enumerate(zip(ys, ys[1:])):
            if not (y0 <= Y0 and Y1 <= y1): continue
            for zi, (Z0, Z1) in enumerate(zip(zs, zs[1:])):
                if not (z0 <= Z0 and Z1 <= z1): continue
                reactor[xi*ystep + yi*zstep + zi] = c

out = 0
for xi, (X0, X1) in enumerate(zip(xs, xs[1:])):
    for yi, (Y0, Y1) in enumerate(zip(ys, ys[1:])):
        for zi, (Z0, Z1) in enumerate(zip(zs, zs[1:])):
            if reactor[xi*ystep + yi*zstep + zi]:
                out += (X1 - X0) * (Y1 - Y0) * (Z1 - Z0)
print(out)
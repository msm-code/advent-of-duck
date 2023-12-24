import re
from sympy import symbols, Eq, solve
Px, Py, Pz, Dx, Dy, Dz = symbols('px py pz dx dy dz')
data = open("input").read().strip()

hail = re.findall("(-?\\d+), +(-?\\d+), +(-?\\d+) @ +(-?\\d+), +(-?\\d+), +(-?\\d+)", data)
hail = [tuple(int(e) for e in h) for h in hail]

tis, eqs = [], []
for i, (px, py, pz, dx, dy, dz) in enumerate(hail[:3]):
    tis.append(ti := symbols(f't{i}'))
    eqs += [Eq(px + dx*ti, Px + Dx*ti), Eq(py + dy*ti, Py + Dy*ti), Eq(pz + dz*ti, Pz + Dz*ti)]

solution = solve(eqs, (Px, Py, Pz, Dx, Dy, Dz) + tuple(tis))
print(sum(solution[0][:3]))

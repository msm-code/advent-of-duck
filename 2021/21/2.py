import re
from functools import cache

pls = [(int(p), 0) for p in re.findall("position: (.+)", open("input").read())]
bimod = [a+b+c+3 for a in range(3) for b in range(3) for c in range(3)]
def update(p, x): return (r := (p[0] + x - 1) % 10 + 1, p[1] + r)

@cache
def stats(pls):
    if pls[1][1] >= 21:
        return (0, 1)
    return [sum(p) for p in zip(*[stats((pls[1], update(pls[0], i))) for i in bimod])][::-1]

print(stats(tuple(pls))[0])
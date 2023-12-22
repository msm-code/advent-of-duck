data = open("input").read().strip().split("\n")

possible = set()
for y in range(len(data)):
    if "S" in data[y]:
        possible.add((data[y].index("S"), y))
        data[y] = data[y].replace("S", ".")

DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def addv(a, b): return (a[0] + b[0], a[1] + b[1])
def legal(pos): return data[pos[1] % len(data)][pos[0] % len(data[0])] == '.'

def update(possible):
    newpossible = set()
    for pos in possible:
        for dir in DIRS:
            newp = addv(pos, dir)
            if legal(newp): newpossible.add(newp)
    return newpossible

for i in range(65):
    possible = update(possible)
x0 = len(possible)

for i in range(262):
    possible = update(possible)
x1 = len(possible)

for i in range(262):
    possible = update(possible)
x2 = len(possible)

d0 = x1 - x0
d1 = x2 - x1
dd = d1 - d0

steps = 26501365
assert steps % 262 == 65
iters = (steps - 65) // 262
print(x0 + iters*d0 + (iters-1)*(iters)//2*dd)

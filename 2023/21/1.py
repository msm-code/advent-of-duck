data = open("input").read().strip().split("\n")

possible = set()
for y in range(len(data)):
    if "S" in data[y]:
        possible.add((data[y].index("S"), y))
        data[y] = data[y].replace("S", ".")

DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def addv(a, b): return (a[0] + b[0], a[1] + b[1])
def legal(pos): return 0 <= pos[0] < len(data[0]) and 0 <= pos[1] < len(data) and data[pos[1]][pos[0]] == '.'

def update(possible):
    newpossible = set()
    for pos in possible:
        for dir in DIRS:
            newp = addv(pos, dir)
            if legal(newp): newpossible.add(newp)
    return newpossible

for i in range(64):
    possible = update(possible)
print(len(possible))

data0 = open('input').read().split()
data0 = [[int(c) for c in row] for row in data0]

def wrap(x):
    return (x - 1) % 9 + 1

SZ = len(data0)
data = [[0] * SZ * 5 for _ in range(SZ * 5)]
for y in range(SZ * 5):
    for x in range(SZ * 5):
        data[y][x] = wrap(data0[y % SZ][x % SZ] + (x // SZ) + (y // SZ))

infinity = 0xffffffff
best = [[infinity for c in row] for row in data]
thebest = infinity
while True:
    for y in range(len(data)):
        for x in range(len(data[y])):
            if x == y == 0:
                best[y][x] = 0
                continue
            bestT = infinity if y == 0 else best[y-1][x]
            bestL = infinity if x == 0 else best[y][x-1]
            bestB = infinity if y == len(best) - 1 else best[y+1][x]
            bestR = infinity if x == len(best) - 1 else best[y][x+1]
            best[y][x] = data[y][x] + min(bestT, bestL, bestB, bestR)
    if best[-1][-1] == thebest:
        break
    thebest = best[-1][-1]

print(thebest)
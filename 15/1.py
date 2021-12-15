data = open('input').read().split()
data = [[int(c) for c in row] for row in data]
best = [[0 for c in row] for row in data]

infinity = 0xffffffff
data[0][0] = -infinity
for y in range(len(data)):
    for x in range(len(data[y])):
        bestY = infinity if y == 0 else best[y-1][x]
        bestX = infinity if x == 0 else best[y][x-1]
        best[y][x] = data[y][x] + min(bestY, bestX)

print(best[-1][-1])
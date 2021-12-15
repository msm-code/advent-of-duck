import re

points, folds = open('input').read().split("\n\n")
points = set(tuple(p.split(',')) for p in points.split())
points = set((int(x), int(y)) for (x, y) in points)
folds = re.findall("fold along (.)=(.+)", folds)

def foldx(points, fx):
    return set(((x if x < fx else fx - (x - fx)), y) for (x, y) in points)

def foldy(points, fy):
    return set((x, (y if y < fy else fy - (y - fy))) for (x, y) in points)

for tpe, f in folds:
    points = {"x": foldx, "y": foldy}[tpe](points, int(f))

result = [[" "] * 80 for _ in range(8)]
for x, y in points:
    result[y][x] = "#" 

print("\n".join("".join(r) for r in result))
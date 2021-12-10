import math
visited = set()

def basin(data, x, y):
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    todo = [(x, y)]
    total = 0
    while todo:
        x, y = todo.pop()
        if (x, y) in visited:
            continue
        if x <= 0 or y <= 0 or x >= len(data) or y >= len(data[0]) or data[x][y] == "9":
            continue
        total += 1
        visited.add((x, y))
        for (dx, dy) in dirs:
            todo.append((x + dx, y + dy))
    return total

data = open('input').read().split()
basins = [basin(data, x, y) for x in range(len(data)) for y in range(len(data[0]))]
print(math.prod(sorted(basins)[-3:]))
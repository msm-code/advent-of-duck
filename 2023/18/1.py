import re

data = open("input", "r").read()
dirmap = { "R": (1, 0), "L": (-1, 0), "D": (0, 1), "U": (0, -1) }
def addv(a, b): return (a[0] + b[0], a[1] + b[1])
def follow(dir, pos): return addv(dirmap[dir], pos)

world = {(0, 0): "#"}
digger = (0, 0)
for dir, steps, color in re.findall("(.) (\\d+) [(]#(......)[)]", data):
    for i in range(int(steps)):
        digger = follow(dir, digger)
        world[digger] = "#"

point_in_interior = [(px+1, py) for (px, py) in sorted(world.keys()) if (px+1, py) not in world][0]
queue = [point_in_interior]
while queue:
    next = queue.pop()
    for dir in dirmap.values():
        newp = addv(dir, next)
        if newp not in world:
            world[newp] = "#"
            queue.append(newp)

print(len(world))

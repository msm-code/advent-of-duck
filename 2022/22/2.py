import re

data = open("input").read()
world, moves = data.split("\n\n")
world = world.split("\n")

# mape the map rectangular
longest_line = max(len(l) for l in world)
world = [l.ljust(longest_line, ' ') for l in world]
# add some margins, so we don't care about bounds too much
world = [list(" " * len(world[0]) + "  ")] + [list(" " + l + " ") for l in world] + [list("  " + " " * len(world[0]))]

# parse the moves
plan = re.findall(r"(\d+|L|R)", moves)

DIRS = ">v<^"

def find_initial_pos(world):
    for y, row in enumerate(world):
        for x, char in enumerate(row):
            if char == '.':
                return '>', (y, x)
    raise RuntimeError()

def in_cube(world, y, x):  # are we in empty space or in cube?
    return world[y][x] in '.#'

def follow_along_the_edge(facing, world, y, x):
    """ Clockwise. Gen all positions along. I could golf this if I wanted """
    y1, x1 = y, x
    facing = DIRS[(DIRS.find(facing) + 2) % 4]
    while True:
        if facing == "<":
            if in_cube(world, y+1, x):
                facing = "v"
                yield "L", facing, (y, x)
            elif not in_cube(world, y+1, x-1):
                y += 1
                x -= 1
                facing = "^"
                yield "R", facing, (y, x)
            else:
                y += 1
        elif facing == ">":
            if in_cube(world, y-1, x):
                facing = "^"
                yield "L", facing, (y, x)
            elif not in_cube(world, y-1, x+1):
                y -= 1
                x += 1
                facing = "v"
                yield "R", facing, (y, x)
            else:
                y -= 1
        elif facing == "v":
            if in_cube(world, y, x+1):
                facing = ">"
                yield "L", facing, (y, x)
            elif not in_cube(world, y+1, x+1):
                facing = "<"
                x += 1
                y += 1
                yield "R", facing, (y, x)
            else:
                x += 1
        elif facing == "^":
            if in_cube(world, y, x-1):
                facing = "<"
                yield "L", facing, (y, x)
            elif not in_cube(world, y-1, x-1):
                y -= 1
                x -= 1
                facing = ">"
                yield "R", facing, (y, x)
            else:
                x -= 1
        yield "F", facing, (y, x)
        if (x1, y1) == (x, y):
            break

def forward(pos, world):
    facing, (y, x) = pos
    y2, x2, facing2 = y, x, facing
    while True:
        if facing2 == ">":
            x2 += 1
        elif facing2 == "<":
            x2 -= 1
        elif facing2 == "^":
            y2 -= 1
        elif facing2 == "v":
            y2 += 1
        else:
            assert False
        if world[y2][x2] == '#':
            return facing, (y, x)
        elif world[y2][x2] == '.':
            return facing2, (y2, x2)
        elif world[y2][x2] == ' ':
            # notfacing is a dumb artifact of my generation method
            # positions in POSMAP are stored "in reverse", so we must flip them
            notfacing = DIRS[(DIRS.find(facing) + 2) % 4]
            facing2, (y2, x2) = POSMAP[(notfacing, (y2, x2))]

def execute_move(pos, world, move):
    if move.isdigit():
        for _ in range(int(move)):
            pos = forward(pos, world)
    else:
        diff = -1 if move == "L" else 1
        pos = DIRS[(DIRS.find(pos[0]) + diff) % 4], pos[1]
    return pos

def execute(pos, world, plan):
    for move in plan:
        pos = execute_move(pos, world, move)
    return pos


initial_pos = find_initial_pos(world)
POSMAP = {}

# we know that at initial position we can start our path from top
path = list(follow_along_the_edge("^", world, initial_pos[1][0] - 1, initial_pos[1][1]))
for i, (move, facing, pos) in enumerate(path):
    if move != "L":  # we only care about left turns
        continue
    lptr, rptr = i - 1, i + 1
    while True:
        # start at left turn, and map edges to each other 
        lelm, relm = path[lptr % len(path)], path[rptr % len(path)]
        if lelm[0] == relm[0] == "R":
            # when 2 turn rights - break
            break
        # otherwise ignore turns
        elif lelm[0] != "F" and relm[0] == "F":
            lptr -= 1
        elif lelm[0] == "F" and relm[0] != "F":
            rptr += 1
        else:
            lpos, rpos = (lelm[1], lelm[2]), (relm[1], relm[2])
            POSMAP[lpos] = rpos
            POSMAP[rpos] = lpos
            lptr -= 1
            rptr += 1

final_pos = execute(initial_pos, world, plan)

# print("\n".join("".join(x) for x in world2))
facing, (y, x) = final_pos
y, x = y-1, x-1
print((y+1)*1000 + (x+1)*4 + DIRS.find(facing))

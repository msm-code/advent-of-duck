import re

data = open("input").read()
world, moves = data.split("\n\n")
world = world.split("\n")
longest_line = max(len(l) for l in world)
world = [l.ljust(longest_line, ' ') for l in world]
plan = re.findall(r"(\d+|L|R)", moves)

DIRS = ">v<^"

def find_initial_pos(world):
    for y, row in enumerate(world):
        for x, char in enumerate(row):
            if char == '.':
                return '>', (y, x)
    raise RuntimeError()

def forward(pos, world):
    facing, (y, x) = pos
    y2, x2 = y, x
    while True:
        if facing == ">":
            x2 += 1
            if x2 >= len(world[0]):
                x2 = 0
        elif facing == "<":
            x2 -= 1
            if x2 < 0:
                x2 = len(world[0]) - 1
        elif facing == "^":
            y2 -= 1
            if y2 < 0:
                y2 = len(world) - 1
        elif facing == "v":
            y2 += 1
            if y2 >= len(world):
                y2 = 0
        else:
            assert False
        if world[y2][x2] == '#':
            return facing, (y, x)
        elif world[y2][x2] == '.':
            return facing, (y2, x2)

def execute_move(pos, world, move):
    if move.isdigit():
        for _ in range(int(move)):
            pos = forward(pos, world)
    else:
        diff = -1 if move == "L" else 1
        pos = DIRS[(DIRS.find(pos[0]) + diff) % 4], pos[1]
    return pos

def execute(world, plan):
    pos = find_initial_pos(world)
    for move in plan:
        pos = execute_move(pos, world, move)
    return pos

final_pos = execute(world, plan)
facing, (y, x) = final_pos
print((y+1)*1000 + (x+1)*4 + DIRS.find(facing))

data = open("input").read().split("\n")

world = [l[1:-1] for l in data if l][1:-1]
blizzards = []
blizzard_dir = {
    ">": (0, 1),
    "<": (0, -1),
    "^": (-1, 0),
    "v": (1, 0),
}
for y, row in enumerate(world):
    for x, el in enumerate(row):
        if el in blizzard_dir:
            blizzards.append(((y, x), el))

def simulate(blizzards):
    new_blizzards = []
    for (y, x), dir in blizzards:
        dy, dx = blizzard_dir[dir]
        ny, nx = y + dy, x + dx
        if ny < 0:
            ny = len(world) - 1
        if ny >= len(world):
            ny = 0
        if nx < 0:
            nx = len(world[0]) - 1
        if nx >= len(world[0]):
            nx = 0
        new_blizzards.append(((ny, nx), dir))
    return new_blizzards

FINAL_POS = (len(world) - 1, len(world[0]))
INIT_POS = (-1, 0)

def update_reachable(reachable, blizzards):
    possible_moves = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (0, 0),
    ]
    forbidden_pos = set(pos for pos, _ in blizzards)
    new_reachable = set()
    for pos in reachable:
        for move in possible_moves:
            newpos = (pos[0] + move[0], pos[1] + move[1])
            if newpos == INIT_POS or newpos == FINAL_POS:
                new_reachable.add(newpos)
            if newpos in forbidden_pos:
                continue
            if (newpos[0] < 0 or newpos[0] >= len(world)):
                continue
            if newpos[1] < 0 or newpos[1] >= len(world[0]):
                continue
            new_reachable.add(newpos)
    return new_reachable

reachable1 = set([(-1, 0)])
reachable2 = set()
reachable3 = set()
for round_number in range(99999):
    blizzards = simulate(blizzards)
    reachable1 = update_reachable(reachable1, blizzards)
    if FINAL_POS in reachable1:
        reachable2.add(FINAL_POS)
    reachable2 = update_reachable(reachable2, blizzards)
    if INIT_POS in reachable2:
        reachable3.add(INIT_POS)
    reachable3 = update_reachable(reachable3, blizzards)
    if FINAL_POS in reachable3:
        print(round_number+1)
        break

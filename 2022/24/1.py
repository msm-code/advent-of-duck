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

reachable = set([(-1, 0)])
final_pos = (len(world) - 1, len(world[0]) - 1)
init_pos = (-1, 0)
for round_number in range(99999):
    new_reachable = set()
    new_blizzards = simulate(blizzards)
    possible_moves = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
        (0, 0),
    ]
    forbidden_pos = set(pos for pos, _ in new_blizzards)
    for pos in reachable:
        if pos == final_pos:
            print(round_number+1)
            exit()
        for move in possible_moves:
            newpos = (pos[0] + move[0], pos[1] + move[1])
            if newpos in forbidden_pos:
                continue
            if (newpos[0] < 0 or newpos[0] >= len(world)) and newpos != init_pos:
                continue
            if newpos[1] < 0 or newpos[1] >= len(world[0]):
                continue
            new_reachable.add(newpos)
    reachable = new_reachable
    blizzards = new_blizzards

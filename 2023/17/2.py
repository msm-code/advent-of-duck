from queue import PriorityQueue

world = [[int(x) for x in r] for r in open("input", "r").read().strip().split("\n")]

dirmap = { "E": (1, 0), "W": (-1, 0), "S": (0, 1), "N": (0, -1) }
turns = { "E": "NS", "W": "NS", "N": "EW", "S": "EW" }
def addv(a, b): return (a[0] + b[0], a[1] + b[1])
def inworld(pos): return 0 <= pos[0] < len(world[0]) and 0 <= pos[1] < len(world)
def follow(dir, pos): return addv(dirmap[dir], pos)

def nextsteps(state):
    pos, dir, speed = state
    opts = []
    if speed >= 4: opts += [(follow(d, pos), d, 1) for d in turns[dir]]
    if speed < 10: opts.append((follow(dir, pos), dir, speed + 1))
    return [o for o in opts if inworld(o[0])]

bestheat = {}
pq = PriorityQueue()
pq.put((0, ((0, 0), "E", 0)))
pq.put((0, ((0, 0), "S", 0)))

while not pq.empty():    
    (heat, nextq) = pq.get()
    for move in nextsteps(nextq):
        mx, my = move[0]
        newheat = heat + world[my][mx]
        if move not in bestheat or bestheat[move] > newheat:
            bestheat[move] = newheat
            pq.put((newheat, move))

def bestxy(x, y): return min(heat for move, heat in bestheat.items() if move[0] == (x, y) and move[2] >= 4)
print(bestxy(len(world)-1, len(world[0]) - 1))

import re

data = open("input", "r").read()

elms = re.findall(r"Valve (.*) has flow rate=(\d+); tunnels? leads? to valves? (.*)", data)

pressures = {}
connections = {}

for frm, press, paths in elms:
    pressures[frm] = int(press)
    connections[frm] = paths.split(", ")

distances = {key: {} for key in connections.keys()}
for key in connections:
    distances[key] = {key: 999999999999 for key in connections.keys()}
    distances[key][key] = 0
    for value in connections[key]:
        distances[key][value] = distances[value][key] = 1

for k in distances:
    for i in distances:
        for j in distances:
            if distances[i][j] > distances[i][k] + distances[k][j]:
                distances[i][j] = distances[i][k] + distances[k][j]


def recursive_best(pos, to_open, time_left):
    current_best = 0
    for conn in to_open:
        if time_left <= distances[pos][conn] + 1:
            continue

        to_open0 = to_open - set([conn])
        time0 = time_left - distances[pos][conn] - 1
        pressure = pressures[conn] * time0
        pressure0 = recursive_best(conn, to_open0, time0)
        current_best = max(current_best, pressure + pressure0)

    return current_best

print(connections)

to_open = set(k for k, v in pressures.items() if v > 0)
best = recursive_best("AA", to_open, 30)
print(best)

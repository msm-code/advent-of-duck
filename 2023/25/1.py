from collections import defaultdict
graph = defaultdict(list)
for l in open("input").read().strip().split("\n"):
    frm, tos = l.split(": ")
    for to in tos.split():
        graph[frm].append(to)
        graph[to].append(frm)
nodes = list(graph.keys())

def dfs(graph, start, to, forbidden):
    q, parent = [start], {start: start}
    while q:
        n = q.pop()
        for el in graph[n]:
            if (n, el) in forbidden or (el, n) in forbidden: continue
            if el == to:
                forbidden.add((el, n))
                while n != start:
                    forbidden.add((n, parent[n]))
                    n = parent[n]
                return True
            if el not in parent:
                q.append(el)
                parent[el] = n
    return False

def flow(start, to):
    f, forbidden = 0, set()
    while dfs(graph, start, to, forbidden): f += 1
    return f

start = nodes[0]
grpa, grpb = {start}, set()
for to in nodes:
    if to == start: continue
    if flow(to, start) > 3: grpa.add(to)
    else: grpb.add(to)
print(len(grpa) * len(grpb))

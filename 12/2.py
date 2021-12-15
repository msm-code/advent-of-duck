data = [x.split("-") for x in open('input').read().split()]
data = data + [x[::-1] for x in data]


def allowed(visited, new):
    if new not in visited:
        return True
    if new in ['start', 'end']:
        return False
    if visited.count(new) == 1 and len(set(visited)) == len(visited):
        return True
    return False


def search(caves, visited, pos, target, path):
    if pos == target:
        return 1
    ways = 0
    elm = [pos] if pos.islower() else []
    for frm, to in caves:
        if not allowed(visited + elm, to):
            continue
        if frm == pos:
            ways += search(caves, visited + elm, to, target, path + [pos])
    return ways


print(search(data, [], 'start', 'end', []))
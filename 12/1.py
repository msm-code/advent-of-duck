data = [x.split("-") for x in open('input').read().split()]
data = data + [x[::-1] for x in data]


def search(caves, visited, pos, target, path):
    if pos == target:
        return 1
    ways = 0
    elm = [pos] if pos.islower() else []
    for frm, to in caves:
        if to in visited:
            continue
        if frm == pos:
            ways += search(caves, visited + elm, to, target, path + [pos])
    return ways


print(search(data, ['start'], 'start', 'end', ['start']))
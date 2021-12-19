import itertools


def rotate_xy(v): return (v[1], -v[0], v[2])
def rotate_xz(v): return (v[2], v[1], -v[0])
def rotate_yz(v): return (v[0], v[2], -v[1])
def vsub(a, b): return (a[0] - b[0], a[1] - b[1], a[2] - b[2])
def vadd(a, b): return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def rotations(vec):
    unique = set(next(iter(vec)))
    for xy in range(2):  # 2 are enough apparently
        vec = [rotate_xy(v) for v in vec]
        for xz in range(4):
            vec = [rotate_xz(v) for v in vec]
            for yz in range(4):
                vec = [rotate_yz(v) for v in vec]
                if next(iter(vec)) not in unique:
                    unique.add(next(iter(vec)))  # (incorrect) check to ignore repeats
                    yield vec


def match(a, template):
    for b in rotations(template):
        for pa in a:
            for pb in b:
                shift = vsub(pa, pb)
                if sum(vadd(p, shift) in a for p in b) >= 12:
                    return a | set(vadd(p, shift) for p in b if vadd(p, shift) not in a)
    return None


scanners = open('input').read().split('scanner')
scanners = [
    set(tuple(int(c) for c in line.split(',')) for line in scanner.split("\n")[1:-1] if line)
    for scanner in scanners if len(scanner.split("\n")) > 1
]

result = scanners.pop()
while scanners:
    for scanner in scanners:
        if glued := match(result, scanner):
            result = glued
            scanners.remove(scanner)
            break
print(len(result))
class Fish:
    def __init__(self, n):
        self.n = n

    @property
    def isint(self):
        return isinstance(self.n, int)

    def __repr__(self):
        return f"🐟{self.n}"


def wrap(nums):
    if isinstance(nums, int):
        return Fish(nums)
    return Fish(list(map(wrap, nums)))


def explode(num, lparent=Fish(0), rparent=Fish(0), depth=0):
    if num.isint:
        return False
    l, r = num.n
    if depth == 4:
        num.n = 0
        while not lparent.isint:
            lparent = lparent.n[1]
        lparent.n += l.n
        while not rparent.isint:
            rparent = rparent.n[0]
        rparent.n += r.n
        return True
    return explode(l, lparent, r, depth+1) or explode(r, l, rparent, depth+1)


def split(num):
    if num.isint:
        if num.n >= 10:
            num.n = [Fish(num.n // 2), Fish((num.n + 1) // 2)]
            return True
        return False
    l, r = num.n
    return split(l) or split(r)


def reduce(num):
    while explode(num) or split(num):
        pass
    return num


def magnitude(num):
    if num.isint:
        return num.n
    return 3*magnitude(num.n[0]) + 2*magnitude(num.n[1])


def clone(num):
    if num.isint:
        return Fish(num.n)
    return Fish([clone(num.n[0]), clone(num.n[1])])


nums = [wrap(eval(x)) for x in open("input").read().split()]
mag = 0
for a in nums:
    for b in nums:
        if a != b:
            mag = max(magnitude(reduce(Fish([clone(a), clone(b)]))), mag)
print(mag)
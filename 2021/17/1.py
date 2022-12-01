import re
data = open('input').read()
x0, x1, y0, y1 = map(int, re.findall("target area: x=([-0-9]+)..([-0-9]+), y=([-0-9]+)..([-0-9]+)", data)[0])
print((-y0 - 1)*(-y0)//2)

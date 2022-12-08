$data = File.open("input").readlines.map(&:chomp)
def inside?(x, y) x.between?(0, $data.size-1) and y.between?(0, $data[0].size-1) end
def visible_from?(x, y, dx, dy, h) not inside?(x, y) or ($data[x][y] < h and visible_from?(x+dx, y+dy, dx, dy, h)) end
def visible?(x, y) [[1, 0], [-1, 0], [0, 1], [0, -1]].any? {|d| visible_from?(x+d[0], y+d[1], d[0], d[1], $data[x][y])} end
p (0..$data.size-1).map {|x| (0..$data[0].size-1).map {|y| visible?(x, y)}}.flatten.map {|x| x ? 1 : 0}.sum

$data = File.open("input").readlines.map(&:chomp)
def inside?(x, y) x.between?(0, $data.size-1) and y.between?(0, $data[0].size-1) end
def dir_score(x, y, dx, dy, h) inside?(x, y) ? ($data[x][y] < h ? 1 + dir_score(x+dx, y+dy, dx, dy, h) : 1) : 0 end
def score(x, y) [[1, 0], [-1, 0], [0, 1], [0, -1]].map {|d| dir_score(x+d[0], y+d[1], d[0], d[1], $data[x][y])}.inject(1, :*) end
p (0..$data.size-1).map {|x| (0..$data[0].size-1).map {|y| score(x, y)}}.flatten.max

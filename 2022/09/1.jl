import Base.parse

DIRS = Dict("L"=>(-1, 0), "R"=>(1, 0), "U"=>(0, -1), "D"=>(0, 1))

parse(line) = let (x, y) = split(line, " "); [DIRS[x] for _ in 1:parse(Int, y)] end
add((ax, xy), (bx, by))::Tuple = (ax+bx, xy+by)
follow((tx, ty), (hx, hy)) = let newpos = (tx + sign(hx - tx), ty + sign(hy - ty))
    if newpos == (hx, hy); (tx, ty) else newpos end
    end

head = (0, 0)
tail = (0, 0)
positions = Set([tail])
lines = [(map(parse, readlines(open("input")))...)...]
for cmd in lines
    global head = add(head, cmd)
    global tail = follow(tail, head)
    push!(positions, tail)
end
println(length(positions))

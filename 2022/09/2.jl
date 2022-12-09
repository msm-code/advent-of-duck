import Base.parse

DIRS = Dict("L"=>(-1, 0), "R"=>(1, 0), "U"=>(0, -1), "D"=>(0, 1))

parse(line) = let (x, y) = split(line, " "); [DIRS[x] for _ in 1:parse(Int, y)] end
add((ax, ay), (bx, by))::Tuple = (ax+bx, ay+by)
follow((tx, ty), (hx, hy)) = let newpos = (tx + sign(hx - tx), ty + sign(hy - ty))
    if newpos == (hx, hy); (tx, ty) else newpos end
    end

rope = [(0, 0) for _ in 1:10]
positions = Set([rope[10]])
lines = [(map(parse, readlines(open("input")))...)...]
for cmd in lines
    rope[1] = add(rope[1], cmd)
    for i in 1:9
        rope[i+1] = follow(rope[i+1], rope[i])
    end
    push!(positions, rope[10])
end
println(length(positions))

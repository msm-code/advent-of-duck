cache = Dict{Int, Int}()
function handle(ndx::Int, line::String)
    if haskey(cache, ndx) return cache[ndx] end
    m = match(r"Card .*: (.*) [|] (.*)", line)
    nums, winning = split(m[1]), split(m[2])
    ok = filter(x -> x in winning, nums)
    cache[ndx] = 1 + sum([handle(j, data[j]) for j=range(ndx+1, ndx+length(ok))], init=0)
end

data = readlines("input")
println(sum([handle(i, s) for (i,s)=enumerate(data)]))

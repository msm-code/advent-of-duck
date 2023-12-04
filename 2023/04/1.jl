function handle(line::String)
    m = match(r"Card .*: (.*) [|] (.*)", line)
    nums, winning = split(m[1]), split(m[2])
    ok = filter(x -> x in winning, nums)
    isempty(ok) ? 0 : 2^(length(ok) - 1)
end

println(sum(map(handle, readlines("input"))))

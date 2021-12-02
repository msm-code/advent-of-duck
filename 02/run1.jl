import Base.parse
using Setfield
using Match

struct State
    distance::Int
    depth::Int
end

struct Forward step::Int end
struct Sink depth::Int end

update(state::State, cmd::Forward) = @set state.distance = state.distance + cmd.step
update(state::State, cmd::Sink) = @set state.depth = state.depth + cmd.depth

parse(cmd::String)::Any = @match split(cmd) begin
    ["forward", n] => Forward(parse(Int, n))
    ["down", n] => Sink(parse(Int, n))
    ["up", n] => Sink(-parse(Int, n))
end

result = foldl(update, map(parse, readlines("input")), init=State(0, 0))
print(result.distance * result.depth)

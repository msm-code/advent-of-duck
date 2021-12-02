import Base.parse
using Setfield
using Match

struct State
    aim::Int
    distance::Int
    depth::Int
end

struct Forward step::Int end
struct Aim direction::Int end

update(state::State, cmd::Forward) = setproperties(state, (
    distance = state.distance + cmd.step,
    depth = state.depth + state.aim * cmd.step
))
update(state::State, cmd::Aim) = @set state.aim = state.aim + cmd.direction

parse(cmd::String)::Any = @match split(cmd) begin
    ["forward", n] => Forward(parse(Int, n))
    ["down", n] => Aim(parse(Int, n))
    ["up", n] => Aim(-parse(Int, n))
end

result = foldl(update, map(parse, readlines("input")), init=State(0, 0, 0))
print(result.distance * result.depth)

const std = @import("std");

pub fn main() !void {
    var file = try std.fs.cwd().openFile("input", .{});
    defer file.close();

    var in_stream = std.io.bufferedReader(file.reader()).reader();

    var state = [_]u16{0} ** 2048;
    var buf: [32]u8 = undefined;
    while (try in_stream.readUntilDelimiterOrEof(&buf, ',')) |num| {
        var slice = if (num[num.len - 1] == '\n') num[0..num.len - 1] else num;
        state[try std.fmt.parseInt(u32, slice, 10)] += 1;
    }

    var best: i32 = std.math.maxInt(i32);
    for (state) |_, tested| {
        var fuel: i32 = 0;
        for (state) |elm, position| {
            var dist = (try std.math.absInt(@intCast(i32, position) - @intCast(i32, tested)));
            fuel += @divExact(dist * (dist+1), 2) * elm;
        }
        best = std.math.min(best, fuel);
    }

    try std.io.getStdOut().writer().print("{d}\n", .{best});
}

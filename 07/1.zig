const std = @import("std");

pub fn main() !void {
    var file = try std.fs.cwd().openFile("input", .{});
    defer file.close();

    var state = [_]u16{0} ** 2048;
    var buf: [32]u8 = undefined;
    var count: u32 = 0;
    var fuel: u64 = 0;
    var in_stream = std.io.bufferedReader(file.reader()).reader();
    while (try in_stream.readUntilDelimiterOrEof(&buf, ',')) |num| {
        var slice = if (num[num.len - 1] == '\n') num[0..num.len - 1] else num;
        var position = try std.fmt.parseInt(u32, slice, 10);
        state[position] += 1;
        fuel += position;
        count += 1;
    }

    var left: u32 = 0;
    var best: u64 = fuel;
    for (state) |elm, position| {
        best = std.math.min(best, fuel);
        left += elm;
        fuel += left;
        fuel -= (count - left);
    }

    try std.io.getStdOut().writer().print("{}\n", .{best});
}

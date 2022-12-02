const std = @import("std");

const RPS = enum {
    Rock,
    Paper,
    Scissors,
};

fn shape_points(shape: RPS) u32 {
    return switch (shape) {
        RPS.Rock => 1,
        RPS.Paper => 2,
        RPS.Scissors => 3,
    };
}

fn points(player: RPS, enemy: RPS) u32 {
    var points_for_shape = shape_points(player);
    var point_for_outcome = (4 + shape_points(player) - shape_points(enemy)) % 3 * 3;
    return points_for_shape + point_for_outcome;
}

pub fn main() !void {
    var file = try std.fs.cwd().openFile("input", .{});
    defer file.close();

    var buf_reader = std.io.bufferedReader(file.reader());
    var in_stream = buf_reader.reader();

    var buf: [1024]u8 = undefined;
    var sum: u32 = 0;
    while (try in_stream.readUntilDelimiterOrEof(&buf, '\n')) |line| {
        var it = std.mem.split(u8, line, " ");
        var enemy = switch (it.first()[0]) {
            'A' => RPS.Rock,
            'B' => RPS.Paper,
            'C' => RPS.Scissors,
            else => std.debug.panic("no bueno", .{}),
        };
        var player = switch (it.next().?[0]) {
            'X' => RPS.Rock,
            'Y' => RPS.Paper,
            'Z' => RPS.Scissors,
            else => std.debug.panic("dick move", .{}),
        };
        sum += points(player, enemy);
    }
    try std.io.getStdOut().writer().print("{}", .{sum});
}

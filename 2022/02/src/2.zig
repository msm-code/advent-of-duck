const std = @import("std");

const RPS = enum {
    Rock,
    Paper,
    Scissors,
};

const Outcome = enum {
    Lose,
    Draw,
    Win,
};

fn shape_points(shape: RPS) u32 {
    return switch (shape) {
        RPS.Rock => 1,
        RPS.Paper => 2,
        RPS.Scissors => 3,
    };
}

fn points_to_shape(pts: u32) RPS {
    return switch (pts) {
        1 => RPS.Rock,
        2 => RPS.Paper,
        3 => RPS.Scissors,
        else => std.debug.panic("dick move", .{}),
    };
}

fn outcome_to_int(outcome: Outcome) u32 {
    return switch(outcome) {
        Outcome.Lose => 2,
        Outcome.Draw => 0,
        Outcome.Win => 1,
    };
}

fn with_outcome(enemy: RPS, outcome: Outcome) RPS {
    var enemypts = shape_points(enemy);
    var mod = outcome_to_int(outcome);
    var player = points_to_shape((enemypts + mod - 1) % 3 + 1);
    return player;
}

fn points(enemy: RPS, outcome: Outcome) u32 {
    var player = with_outcome(enemy, outcome);
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
        var outcome = switch (it.next().?[0]) {
            'X' => Outcome.Lose,
            'Y' => Outcome.Draw,
            'Z' => Outcome.Win,
            else => std.debug.panic("i'm a secret fourth thing", .{}),
        };
        sum += points(enemy, outcome);
    }
    try std.io.getStdOut().writer().print("{}", .{sum});
}

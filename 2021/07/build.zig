const std = @import("std");

pub fn build(b: *std.build.Builder) void {
    const target = b.standardTargetOptions(.{});

    const mode = b.standardReleaseOptions();

    const exe1 = b.addExecutable("1", "1.zig");
    exe1.setTarget(target);
    exe1.setBuildMode(mode);
    exe1.install();

    const exe2 = b.addExecutable("2", "2.zig");
    exe2.setTarget(target);
    exe2.setBuildMode(mode);
    exe2.install();
}

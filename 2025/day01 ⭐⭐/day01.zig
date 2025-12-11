const std = @import("std");

pub fn main() !void {
    var it, var dail: i64, var p1: u64, var p2: u64 = .{ std.mem.splitScalar(u8, @embedFile("input"), '\n'), 50, 0, 0 };
    while (it.next()) |ln| {
        var dist: i32 = if (ln.len > 1) try std.fmt.parseInt(u16, ln[1..(ln.len - 1)], 10) else continue;
        while (dist > 0) : (dist -= 1) {
            dail += if (ln[0] == 'R') 1 else -1;
            if (ln[0] == 'L' and dail < 0) dail = 99;
            if (ln[0] == 'R' and dail > 99) dail = 0;
            if (dail == 0) p2 += 1;
        } else if (dail == 0) p1 += 1;
        // dist *= if (ln[0] == 'R') 1 else -1;
        // p2 += @abs(@divTrunc(dail - @intFromBool(dist > 0), 100) - @divTrunc(dail + dist - @intFromBool(dist < 0), 100));
        // dail += dist;
        // p1 += @intFromBool(@mod(dail, 100) == 0);
    } else std.debug.print("first {}\nsecond {}\n", .{ p1, p2 });
}

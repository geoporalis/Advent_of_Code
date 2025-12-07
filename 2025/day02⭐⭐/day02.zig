const std = @import("std");

var start: usize = 0;
var end: usize = 0;

pub fn main() !void {
    var it, var p1: u64, var p2: u64 = .{ std.mem.splitScalar(u8, @embedFile("input"), ','), 0, 0 };

    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    defer _ = gpa.deinit();
    const allocator = gpa.allocator();

    while (it.next()) |ln| {
        var it2 = std.mem.splitScalar(u8, ln, '-');
        start = try std.fmt.parseUnsigned(usize, it2.next().?, 10);
        end = try std.fmt.parseUnsigned(usize, it2.next().?, 10);

        for (start..(end + 1)) |num| {
            const s = try std.fmt.allocPrint(allocator, "{d}", .{num});
            defer allocator.free(s);

            for (1..s.len) |k| {
                const ss = s[0..k];
                if (s.len % k != 0) continue;
                if (std.mem.count(u8, s, ss) == s.len / k) {
                    p2 += num;
                    break;
                }
            }
            if (s.len % 2 != 0) continue;
            if (std.mem.eql(u8, s[0..(s.len / 2)], s[(s.len / 2)..])) p1 += num;
        }
    } else std.debug.print("first {}\nsecond {}\n", .{ p1, p2 });
}

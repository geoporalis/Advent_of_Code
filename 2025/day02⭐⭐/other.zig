var result: Result = .{ .p1 = 0, .p2 = 0 };

var i: usize = 0;
var j: usize = 0;
var ranges = std.mem.splitScalar(u8, data, ',');

while (ranges.next()) |line| {
    var it = std.mem.splitScalar(u8, line, '-');

    i = try std.fmt.parseUnsigned(usize, it.next().?, 10);
    j = try std.fmt.parseUnsigned(usize, it.next().?, 10);

    for (i..(j + 1)) |num| {
        const s = try std.fmt.allocPrint(allocator, "{d}", .{num});
        defer allocator.free(s);

        for (1..s.len) |k| {
            const ss = s[0..k];
            if (s.len % ss.len != 0) continue;

            if (std.mem.count(u8, s, ss) == s.len / ss.len) {
                result.p2 += num;
                break;
            }
        }

        if (s.len % 2 != 0) continue;

        if (std.mem.eql(u8, s[0..(s.len / 2)], s[(s.len / 2)..])) 
            result.p1 += num;
        }
    }
}
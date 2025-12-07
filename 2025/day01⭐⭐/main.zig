const std = @import("std");

pub const input = @embedFile("input");

fn part1(data: []const u8) !i16 {
    var result: i16 = 0;
    var pos: i16 = 50;
    var it = std.mem.splitScalar(u8, data, '\n');
    while (it.next()) |ln| {
        if (ln.len == 0) continue;
        std.debug.print("line {s}", .{ln});
        const steps = try std.fmt.parseInt(i16, ln[1..], 10);
        pos = @mod(pos + if (ln[0] == 'L') -steps else steps, 100);
        if (pos == 0) result += 1;
    }
    return result;
}

fn part2(data: []const u8) !i16 {
    var result: i16 = 0;
    var pos: i16 = 50;
    var it = std.mem.splitScalar(u8, data, '\n');
    while (it.next()) |ln| {
        if (ln.len == 0) continue;
        const steps = try std.fmt.parseInt(i16, ln[1..], 10);
        result += @divTrunc(steps, 100);
        const rest = @mod(steps, 100);
        if (rest == 0) continue;
        const next = pos + if (ln[0] == 'L') -rest else rest;
        if (pos != 0 and (next <= 0 or next >= 100)) result += 1;
        pos = @mod(next, 100);
    }
    return result;
}

pub fn main() !void {
    std.debug.print("{d}\n", .{try part1(input)});
    std.debug.print("{d}\n", .{try part2(input)});
}
// const std = @import("std");
// const input = @embedFile("input");
// // pub fn main() void {
// //     std.debug.print("Hello, {s}!\n", .{"World"});
// // }
// // https://cookbook.ziglang.cc/01-01-read-file-line-by-line.html

// const fs = std.fs;
// const print = std.debug.print;

// pub fn main() !void {
//     // for (input) |byte| {
//     //     print("{d}", .{byte});
//     // }
//     var it = std.mem.tokenizeScalar(u8, input, '\n');
//     while (it.next()) |token| {
//         var nit = std.mem.tokenizeScalar(u8, token, ' ');
//         while (nit.next()) |tokn| {
//             print("{s}\n", .{tokn});
//         }
//     }

//     // var gpa = std.heap.GeneralPurposeAllocator(.{}){};
//     // defer _ = gpa.deinit();
//     // const allocator = gpa.allocator();

//     // const file = try fs.cwd().openFile("../input", .{});
//     // defer file.close();

//     // // Wrap the file reader in a buffered reader.
//     // // Since it's usually faster to read a bunch of bytes at once.
//     // var buf_reader = std.io.bufferedReader(file.reader());
//     // const reader = buf_reader.reader();

//     // var line = std.ArrayList(u8).init(allocator);
//     // defer line.deinit();

//     // const writer = line.writer();
//     // var line_no: usize = 0;
//     // while (reader.streamUntilDelimiter(writer, '\n', null)) {
//     //     // Clear the line so we can reuse it.
//     //     defer line.clearRetainingCapacity();
//     //     line_no += 1;
//     //     var it = std.mem.splitScalar(u8, line.items, ' ');
//     //     const xt = std.fmt.parseInt(i32, it.first(), 10);
//     //     const yt = std.fmt.parseInt(i32, it[1], 10);
//     //     print("{d}: {d} - {d} = {d}\n", .{ line_no, xt, yt, (xt - yt) });

//     //     // while (it.next()) |x| {
//     //     //     print("{s}", .{x});
//     //     // }

//     //     // print("{}\n", .{" "});
//     // } else |err| switch (err) {
//     //     error.EndOfStream => { // end of file
//     //         if (line.items.len > 0) {
//     //             line_no += 1;
//     //             print("{d} -> {s}\n", .{ line_no, line.items });
//     //         }
//     //     },
//     //     else => return err, // Propagate error
//     // }

//     // print("Total lines: {d}\n", .{line_no});
// }

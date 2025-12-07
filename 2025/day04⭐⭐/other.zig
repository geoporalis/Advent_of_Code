const std = @import("std");

pub const input = @embedFile("input");

fn part1(data: []const u8) !u64 {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    const allocator = gpa.allocator();

    var grid = try std.ArrayList([]const u8).initCapacity(allocator, 0);
    defer grid.deinit(allocator);

    var lines = std.mem.splitScalar(u8, data, '\n');
    while (lines.next()) |line| {
        if (line.len > 0) {
            try grid.append(allocator, line);
        }
    }
    const height: u64 = grid.items.len;
    const width: u64 = grid.items[0].len;

    var rolls: u64 = 0;
    for (0..height) |y| {
        const row = grid.items[y];
        for (0..width) |x| {
            if (row[x] == '.') continue;
            var neighbors: usize = 0;
            for ([_]isize{ -1, 0, 1 }) |dy| {
                for ([_]isize{ -1, 0, 1 }) |dx| {
                    if (dx == 0 and dy == 0) continue;
                    const nx: isize = @as(isize, @intCast(x)) + dx;
                    const ny: isize = @as(isize, @intCast(y)) + dy;
                    if (nx < 0 or nx >= width or ny < 0 or ny >= height) continue;
                    if (grid.items[@intCast(ny)][@intCast(nx)] == '@') {
                        neighbors += 1;
                    }
                }
            }
            if (neighbors < 4) {
                rolls += 1;
            }
        }
    }
    return rolls;
}

fn part2(data: []const u8) !u64 {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    const allocator = gpa.allocator();

    var grid = try std.ArrayList([]u8).initCapacity(allocator, 0);
    defer grid.deinit(allocator);

    var lines = std.mem.splitScalar(u8, data, '\n');
    while (lines.next()) |line| if (line.len > 0) try grid.append(allocator, try allocator.dupe(u8, line));

    const height: u64 = grid.items.len;
    const width: u64 = grid.items[0].len;
    const checks = [_]struct { i8, i8 }{ .{ 0, 1 }, .{ 1, 1 }, .{ 1, 0 }, .{ 1, -1 }, .{ 0, -1 }, .{ -1, -1 }, .{ -1, 0 }, .{ -1, 1 } };

    var changed = true;
    var rolls: u64 = 0;
    while (changed) {
        changed = false;
        for (0..height) |y| {
            for (0..width) |x| {
                if (grid.items[y][x] == '.') continue;
                var neighbors: i64 = 0;
                for (checks) |check| {
                    const nx: isize, const ny: isize = .{ @as(isize, @intCast(x)) + check[0], @as(isize, @intCast(y)) + check[1] };
                    if (nx < 0 or nx >= width or ny < 0 or ny >= height) continue;
                    if (grid.items[@intCast(ny)][@intCast(nx)] == '@') neighbors += 1;
                    // }
                }
                if (neighbors < 4) {
                    grid.items[y][x], changed = .{ '.', true };
                    rolls += 1;
                }
            }
        }
    }
    return rolls;
}

pub fn main() !void {
    // std.debug.print("{d}\n", .{try part1(input)});
    std.debug.print("{d}\n", .{try part2(input)});
}

// const PointSet = std.AutoArrayHashMap(pos.Point, void);

// pub fn removePaper(allocator: Allocator, paper: *PointSet) !usize {
//     var removable = try std.ArrayList(pos.Point).initCapacity(allocator, 512);
//     defer removable.deinit(allocator);

//     var it = paper.iterator();
//     while (it.next()) |e| {
//         const p = e.key_ptr.*;

//         var cnt: u8 = 0;
//         for (pos.dir8_map.values()) |d|
//             cnt += @intFromBool(paper.contains(p + d));

//         if (cnt < 4) try removable.append(allocator, p);
//     }

//     for (removable.items) |p| _ = paper.swapRemove(p);

//     return removable.items.len;
// }

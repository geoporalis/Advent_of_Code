from pathlib import Path

example = False # True # 

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()

rows = open(file).read().split()

# def argmax(xs):
#     return max(enumerate(xs), key=lambda x: x[1])[0]

# def joltage(row, leave=0):
#     if leave > 0:
#         i = argmax(row[:-leave])
#         return row[i] + joltage(row[i+1:], leave=leave-1)
#     else:
#         return max(row)

# print(sum(int(joltage(row, 1)) for row in rows))
# print(sum(int(joltage(row, 11)) for row in rows))

# def wow_recursion(input_str, len):
#     if len == 0: return []

#     if len == 1: at_least_len = input_str
#     else:        at_least_len = input_str[: -len + 1]

#     highest = 0
#     highest_index = 0

#     for i, c in enumerate(at_least_len):
#         if int(c) > highest:
#             highest = int(c)
#             highest_index = i
#     return [highest] + wow_recursion(input_str[highest_index + 1 :], len - 1)


# total = 0
# for row in rows:
#     best_stuff = wow_recursion(row, 12)
#     for i, digit in enumerate(best_stuff[::-1]):
#         total += digit * (10**i)
# print(total)

def get_twelve_biggest(battery_bank: str, batteries: int) -> int:
    """Extract the 12 largest digits in the order they appear in the string."""
    bank: list[str] = [battery for battery in battery_bank]
    biggest: list[str] = []

    # Iteratively find largest digits, ensuring we reserve space for remaining selections
    # i counts down from 11 to 0, excluding the last i positions from consideration
    for i in range(batteries-1, -1, -1):
        biggest_battery = max(bank[:-i]) if i != 0 else max(bank)
        biggest.append(biggest_battery)
        # Update bank to everything after the selected digit
        bank = bank[bank.index(biggest_battery) + 1 :]

    return int("".join(biggest))

print(f"Total joltage: {sum(get_twelve_biggest(row,  2) for row in rows)}")
print(f"Total joltage: {sum(get_twelve_biggest(row, 12) for row in rows)}")
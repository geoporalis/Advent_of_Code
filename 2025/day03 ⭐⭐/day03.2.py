from pathlib import Path
# import math, re

example = False # True # 

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()
rows = open(file).read().split()

part1 = 0
part2 = 0

def get_biggest_batteries(battery_bank: str, batteries: int) -> int:
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

part1 = sum(get_biggest_batteries(row,  2) for row in rows)
part2 = sum(get_biggest_batteries(row, 12) for row in rows)


sol1 = 357 if example else 17074
sol2 = 3121910778619 if example else 169512729575727
print(part1, (part1 == sol1) , part1 - sol1)
print(part2, (part2 == sol2) , part2 - sol2)



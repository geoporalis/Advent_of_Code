
rules, updates = open('input').read().split('\n\n')
updates = [x.split(',') for x in updates.split('\n')]

def true_pos(x, nums): return len(nums) - 1 - sum(f"{x}|{y}" in rules for y in nums)
def mid(nums): return next(x for x in nums if true_pos(x, nums) == len(nums)//2)
def is_ordered(nums): return all(i == true_pos(x, nums) for i,x in enumerate(nums))

print(sum(int(mid(nums)) for nums in updates if is_ordered(nums)))
print(sum(int(mid(nums)) for nums in updates if not is_ordered(nums)))

##  ~~~~~~~~~~~~~~~~~~~~
rules, updates = open('input').read().split('\n\n')
updates = [x.split(',') for x in updates.split('\n')]

def order(nums): return sorted(nums, key=lambda x: -sum(f"{x}|{y}" in rules for y in nums))

print(sum(int(order(nums)[len(nums)//2]) for nums in updates if order(nums) == nums))
print(sum(int(order(nums)[len(nums)//2]) for nums in updates if order(nums) != nums))

##  ~~~~~~~~~~~~~~~~~~~~

rules, pages = open('input').read().strip().split('\n\n')
rules = {tuple(map(int, x.split('|'))) for x in rules.split()}
pages = [ list(map(int, x.split(','))) for x in pages.split()]

from functools import cmp_to_key
key = cmp_to_key(lambda a, b: ((b, a) in rules) - ((a, b) in rules))

print( sum(new_row[len(row)//2] for row in pages if row == (new_row := sorted(row, key=key))) )
print( sum(new_row[len(row)//2] for row in pages if row != (new_row := sorted(row, key=key))) )
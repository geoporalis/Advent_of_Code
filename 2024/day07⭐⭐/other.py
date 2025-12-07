#!/usr/bin/env pypy3

import sys
from collections import namedtuple
import itertools
from operator import add, mul

from pathlib import Path

dir = Path(__file__).parent.resolve()
file = Path(dir/'input').resolve()

equations = []
Equation = namedtuple('Equation', ['target', 'args'])

for line in open(file).readlines():
  eq, args = line.strip().split(': ')
  equations.append(Equation(int(eq), list(map(int, args.split(' ')))))

def cat(a, b):
  return int(str(a)+str(b))

def find(eq, ops):
  opss = itertools.product(ops, repeat=len(eq.args)-1)
  for ops in opss:
    sumeq = eq.args[0]
    for op, arg in zip(ops, eq.args[1:]):
      sumeq = op(sumeq, arg)
      if eq.target < sumeq:
        break
    if sumeq == eq.target:
      return eq.target
  return 0

def part1():
  return sum(find(eq, (add, mul)) for eq in equations)

def part2():
  return sum(find(eq, (add, mul, cat)) for eq in equations)

print(part1())
# print(part2())

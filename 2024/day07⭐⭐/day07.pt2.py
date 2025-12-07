from colorama import Fore
from pathlib import Path

example = False  #True  #

dir = Path(__file__).parent.resolve()

file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()

def decimal_to_basestring(num, base=3):
    if num == 0:
        return '0'
    base3 = ''
    while num > 0:
        base3 = str(num % base) + base3
        num = num // base
    return base3

caluculations = []
list_of_operators = {}
checksum = 0
bad_list = []

base = 3

for k, l in enumerate(open(file).readlines()):
    sums = []
    result, operands = l.strip().split(': ')
    operands = operands.split(' ')
    operator = ['+', 'x', '|']

    num_operators = len(operands)-1
   
    if not str(num_operators) in list_of_operators.keys():
        operators_list = []
        for i in range(base**num_operators):
            bins = '0'*32 + decimal_to_basestring(i, base)
            binss = ''.join([operator[int(b)] for b in bins[-(num_operators):]])
            operators_list.append([binss])
        list_of_operators[str(num_operators)] = operators_list



    for lo in list_of_operators[str(num_operators)]:
        calc = int(operands[0])
        for i, o in enumerate(lo[0]):
            if o == '+':
                calc += int(operands[i+1])
            if o == 'x':
                calc *= int(operands[i+1])
            if o == '|':
                calc = int(str(calc) + operands[i+1])

            if int(result) < calc:
                break
        sums.append(calc)

        if int(result) == calc:
            break
    

    if int(result) == calc:
        checksum += calc
    else:
        bad_list.append({result: operands})

print('Anser: ', checksum) 

assert checksum == 11387 if example else 271691107779347

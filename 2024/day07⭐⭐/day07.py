from colorama import Fore
from pathlib import Path

example = False  #True  #

dir = Path(__file__).parent.resolve()

file = Path(dir/'input').resolve() if not example else Path(dir/'example').resolve()

caluculations = []
list_of_operators = {}
checksum = 0
bad_list = []
for k, l in enumerate(open(file).readlines()):
    sums = []
    result, operands = l.strip().split(': ')
    operands = operands.split(' ')
    operator = [[['+'], ['*']]]

    # print(l.strip())
    num_operators = len(operands)-1
    
    # '{0:07b}'.format(12) 2^num_operators
    if not str(num_operators) in list_of_operators.keys():
        operators_list = []
        for i in range(2**num_operators):
            bins = '{0:032b}'.format(i)
            binss = ''
            for c in bins[-(num_operators):]:
                if c == '0':
                    binss += '+'
                if c == '1':
                    binss += 'x'
            operators_list.append([binss])
        list_of_operators[str(num_operators)] = operators_list

    for lo in list_of_operators[str(num_operators)]:
        calc = int(operands[0])
        # print(lo)
        for i, o in enumerate(lo[0]):
            if o == '+':
                calc += int(operands[i+1])
            if o == 'x':
                calc *= int(operands[i+1])
            # input(calc)
            if int(result) < calc:
                break
        sums.append(calc)

        # print('\r',result, ':', sums, end='')
        if int(result) == calc:
            break
    

    if int(result) == calc:
        checksum += calc
    else:
        bad_list.append({result: operands})

    print(k, checksum, len(bad_list))

print('Anser: ', checksum) 

assert checksum == 3749 if example else 945512582195


# def decimal_to_base3(num):
#     if num == 0:
#         return '0'
#     base3 = ''
#     while num > 0:
#         base3 = str(num % 3) + base3
#         num = num // 3
#     return base3

assert checksum == 11387 if example else 945512582195

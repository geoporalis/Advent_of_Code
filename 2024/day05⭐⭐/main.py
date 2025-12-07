from pathlib import Path
from colorama import Fore

import math
listOfData = []
dir = Path(__file__).parent.resolve()

with open(Path(dir/'order').resolve() ,'r') as f:
    orderList = [x.strip('\n').split("|") for x in f.readlines()]
with open(Path(dir/'pages').resolve() ,'r') as f:
    pagesList = [x.strip('\n') for x in f.readlines()]

the_good = []
def goodNbaad(orderList, pagesList):
    for order in orderList:
        for i, page in enumerate(pagesList):
            if 'x' in page:
                continue
            if order[0] in page and order[1] in page:
                if page.find(order[0]) < page.find(order[1]):
                    pagesList[i] = pagesList[i].strip('+')+'+'
                else:
                    pagesList[i] = pagesList[i].strip('+')+'x'
    return pagesList



gnbList = goodNbaad(orderList, pagesList)
good_pages = [page for page in gnbList if '+' in page]
bad_pages = [page.strip('x') for page in gnbList if 'x' in page]

print(len(good_pages), len(bad_pages), len(gnbList))

routing = 0
for page in good_pages:
    if '+' in page:
        m = math.floor((len(page)-1)/2)
        routing +=int(page[m-1:m+1])
print(routing) #7307


# my half solution
relevantList=[]
for p, page in enumerate(bad_pages):
    relevant = []
    for order in orderList:
        if order[0] in bad_pages[p] and order[1] in bad_pages[p]:
            relevant.append(order)
    relevantList.append(relevant)

new_page_s = []
for relSubList in relevantList:
    new_page=[]
    for rel in relSubList:
        
        if not rel[0] in new_page:
            new_page.insert(0, rel[0])
        if not rel[1] in new_page:
            new_page.insert(-1, rel[1])

        lidx = new_page.index(rel[0])    
        ridx = new_page.index(rel[1])    
        if ridx < lidx:
            el = new_page.pop(lidx)
            new_page.insert(ridx, el)
    new_page_s.append(",".join(new_page))

ordering = [[int(o[0]), int(o[1])] for o in orderList]
wrong_sequences = [list(map(int, line.split(","))) for line in bad_pages]


# from some one else (bubble sort)
changes = True
while changes:
	changes = False
	for i, sequence in enumerate(wrong_sequences):
		for rule in ordering:
			first_ix = 0
			second_ix = 0
			if rule[0] in sequence and rule[1] in sequence:
				first_ix = sequence.index(rule[0])
				second_ix = sequence.index(rule[1])
				if first_ix > second_ix:
					wrong_sequences[i][first_ix], wrong_sequences[i][second_ix] = wrong_sequences[i][second_ix], wrong_sequences[i][first_ix]
					changes = True
					sequence = wrong_sequences[i]

total = 0
for sequence in wrong_sequences:
	middle_num = sequence[len(sequence)//2]
	total += middle_num

print(Fore.YELLOW, total, Fore.RESET)    

# yet anoter solution
def isOrderd(sequence):
    for rule in ordering:
        if rule[0] in sequence and rule[1] in sequence:
            first_ix = sequence.index(rule[0])
            second_ix = sequence.index(rule[1])
            if first_ix > second_ix:
                return False
    return True

wrong_again_sequences = [list(map(int, line.split(","))) for line in bad_pages]

correct_sequence = []
for pages in wrong_again_sequences:
    while not isOrderd(pages):
        for i in range(len(pages)):
            for j in range(i+1, len(pages)):
                if [pages[j], pages[i]] in ordering:
                    pages[j], pages[i] = pages[i], pages[j]    
    correct_sequence.append(pages)

total = 0
for sequence in correct_sequence:
	middle_num = sequence[len(sequence)//2]
	total += middle_num

print(Fore.MAGENTA, total, Fore.RESET)  
# 4672 to low      

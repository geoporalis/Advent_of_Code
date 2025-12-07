from pathlib import Path
from colorama import Fore

listOfData = []
dir = Path(__file__).parent.resolve()

def calcDiff(report_data):
    report_data_diff = [] 

    for i in range(len(report_data)-1):
        diff = report_data[i]-report_data[i+1]
        diff = 0 if abs(diff) > 3 else diff
        report_data_diff.append(-1 if diff < 0 else 1 if diff > 0 else 0)

    return report_data_diff

with open(Path(dir/'input').resolve() ,'r') as f:
    listOfData = f.readlines()

save_reports = 0
for report in listOfData:
    report_data = [int(x) for x in report.strip('/n').split(' ')]
    report_data_len = len(report_data)
    for i in range(report_data_len):
        report_data_popped = [x for x in report_data]
        report_data_popped.pop(i)
        report_data_diff = calcDiff(report_data_popped)
        if abs(sum(report_data_diff)) == len(report_data_diff):
            save_reports += 1  #
            break

print(Fore.GREEN, save_reports, Fore.RESET)

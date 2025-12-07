from pathlib import Path
from colorama import Fore

listOfData = []
dir = Path(__file__).parent.resolve()

with open(Path(dir/'input').resolve() ,'r') as f:
    listOfData = f.readlines()

save_reports = 0
for report in listOfData: #[:5]:
    report_data = [int(x) for x in report.strip('/n').split(' ')]
    report_data_diff = []
    for i in range(len(report_data)-1):
        diff = report_data[i]-report_data[i+1]
        diff = 0 if abs(diff) > 3 else diff
        report_data_diff.append(-1 if diff < 0 else 1 if diff > 0 else 0)
    save_reports += 1 if abs(sum(report_data_diff)) == len(report_data_diff) else 0

print(Fore.GREEN, save_reports)

import sys
import itertools
import functools


def report_is_safe(report):
    """ returns 1 if report is safe and 0 otherwise """
    
    if report == []:
        return False

    intermediate = [report[i] - report[i+1] for i in range(len(report) - 1)]
    i_length = len(intermediate)
    increasing = all(intermediate[i] < 0 for i in range(i_length))
    decreasing = all(intermediate[i] > 0 for i in range(i_length))
    shallow = all(abs(intermediate[i]) <= 3 and abs(intermediate[i]) >= 1 for i in range(i_length))

    return (increasing or decreasing) and shallow


safe_reports = 0
for line in sys.stdin:
    report = list(map(int, line.split()))
    if report_is_safe(report):
        safe_reports += 1

print(safe_reports)

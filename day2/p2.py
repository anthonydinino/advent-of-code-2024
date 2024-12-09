import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: [program] [input.txt]")
        return
    with open(sys.argv[1], "r") as file:
        count = 0
        for line in file:
            report = [int(num) for num in line.strip().split(" ")]
            increasing = isIncreasing(report)
            if safe(report, increasing):
                count += 1
                print(report)
            else:
                if problemDampener(report, increasing):
                    count += 1
                    print(report)
        print(count)


def safe(report, isIncreasing):
    safe = [-1, -2, -3] if isIncreasing else [1, 2, 3]
    for i in range(len(report) - 1):
        diff = report[i] - report[i + 1]
        if diff not in safe:
            return False
    return True


def problemDampener(report, increasing):
    for i in range(len(report)):
        temp = report[:]
        del temp[i]
        if safe(temp, increasing):
            return True
    return False


def isIncreasing(report):
    diffs = []
    for i in range(len(report) - 1):
        diffs.append(report[i] - report[i + 1])
    res = [num > 0 for num in diffs]
    return res.count(True) < res.count(False)


if __name__ == "__main__":
    main()

from enum import Enum

with open("4/input", "r") as file:
    lines = file.readlines()


class Direction(Enum):
    INCREASING = 1
    DECREASING = 2
    OTHER = 3


res = 0
for j, line in enumerate(lines):
    report = [int(level) for level in line.split(" ")]
    safe = False
    for i in range(len(report)):
        dampened_report = [x for k, x in enumerate(report) if k != i]
        if dampened_report[0] < dampened_report[1] and dampened_report[0] + 3 >= dampened_report[1]:
            direction = Direction.INCREASING
        elif dampened_report[0] > dampened_report[1] and dampened_report[0] - 3 <= dampened_report[1]:
            direction = Direction.DECREASING
        else:
            continue
        for i in range(1, len(dampened_report) - 1):
            if direction.value == Direction.INCREASING.value:
                if dampened_report[i] >= dampened_report[i + 1] or dampened_report[i] + 3 < dampened_report[i + 1]:
                    direction = Direction.OTHER
                    break
            elif direction.value == Direction.DECREASING.value:
                if dampened_report[i] <= dampened_report[i + 1] or dampened_report[i] - 3 > dampened_report[i + 1]:
                    direction = Direction.OTHER
                    break
        if direction.value != Direction.OTHER.value:
            safe = True
            break
    if safe:
        res += 1
        print(f"Report {j} is Safe")
    else:
        print(f"Report {j} is Unsafe")

with open("4/output", "w") as file:
    file.write(str(res))

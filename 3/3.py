from enum import Enum

with open("3/input", "r") as file:
    lines = file.readlines()


class Direction(Enum):
    INCREASING = 1
    DECREASING = 2
    OTHER = 3


res = 0
for j, line in enumerate(lines):
    report = [int(level) for level in line.split(" ")]
    if report[0] < report[1] and report[0] + 3 >= report[1]:
        direction = Direction.INCREASING
    elif report[0] > report[1] and report[0] - 3 <= report[1]:
        direction = Direction.DECREASING
    else:
        continue
    for i in range(1, len(report) - 1):
        if direction.value == Direction.INCREASING.value:
            if report[i] >= report[i + 1] or report[i] + 3 < report[i + 1]:
                direction = Direction.OTHER
                break
        elif direction.value == Direction.DECREASING.value:
            if report[i] <= report[i + 1] or report[i] - 3 > report[i + 1]:
                direction = Direction.OTHER
                break
    if direction.value != Direction.OTHER.value:
        res += 1
        print(f"Report {j} is valid")
    else:
        print(f"Report {j} is invalid")

with open("3/output", "w") as file:
    file.write(str(res))

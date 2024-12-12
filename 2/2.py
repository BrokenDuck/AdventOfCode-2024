from collections import Counter

with open('2/input', 'r') as file:
    lines = file.readlines()

left = []
right = Counter()
for line in lines:
    line = line.strip()
    parsed = line.split("   ")
    left.append(int(parsed[0]))
    right[int(parsed[1])] += 1

res = 0
for l in left:
    res += l*right[l]

with open('2/output', 'w') as file:
    file.write(str(res))
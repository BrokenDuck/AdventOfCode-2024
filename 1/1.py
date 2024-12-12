with open('1/input', 'r') as file:
    lines = file.readlines()

left = []
right = []  
for line in lines:
    line = line.strip()
    parsed = line.split("   ")
    left.append(int(parsed[0]))
    right.append(int(parsed[1]))
    
left.sort()
right.sort()

res = 0
for l, r in zip(left, right):
    diff = l - r
    if diff > 0:
        res += diff
    else:
        res -= diff

with open('1/output', 'w') as file:
    file.write(str(res))
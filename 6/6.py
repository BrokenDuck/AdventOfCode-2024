import re

with open('6/input', 'r') as file:
    text = file.read()
    
res = 0
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
for split in text.split("do()"):
    sub = split.split("don't()")[0]
    for match in re.findall(pattern, sub):
        num1, num2 = map(int, match)
        res += num1*num2

with open('6/output', 'w') as file:
    file.write(str(res))
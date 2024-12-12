import re

with open('5/input', 'r') as file:
    text = file.read()
    
res = 0
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
for match in re.findall(pattern, text):
    num1, num2 = map(int, match)
    res += num1*num2

with open('5/output', 'w') as file:
    file.write(str(res))
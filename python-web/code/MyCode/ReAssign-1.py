import re
hand = open('regex_sum_396137.txt')

sum=0
for line in hand:
    line = line.strip()
    digit = re.findall('[0-9]+',line)
    for add in digit:
        sum+=int(add);

print(sum)
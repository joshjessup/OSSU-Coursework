import re

name = input("Enter File: ")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

sumVal = 0

for line in handle:
    line = line.rstrip()
    numbers = re.findall('[0-9]+', line)
    for number in numbers:
        number = int(number)
        sumVal = sumVal + number

print(sumVal)

###################################################
###################################################
## BONUS ## MUST BE COMPILED SEPARATELY FROM ABOVE OR COMMENTED

import re
print( sum( [ int(i) for i in re.findall('[0-9]+',open('regex_sum_1035759.txt').read()) ] ) )

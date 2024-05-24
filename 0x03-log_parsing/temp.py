#!/usr/bin/env python3


import re

names = ['Finn bindeballe', 'Geir Anders Berge', 'HappyCodingRebot', 'Ron   Cromberge', 'Sohil']

# find people with first/last name only
# start with '^' , sequence of positive number of characters '\w+' ,no more $
def printObj(obj={}):
    print("{", end="")
    for _, __ in obj.items():
        print(f" {_} : {__} ", end="")
    print("}")
regex = '^\w+\s+\w+$'
for name in names:
    res = re.search(regex, name)
    if res:
        printObj({0: res.group()})

x = [name  for name in names if re.search(regex, name)]
print(x)
"""
Author : Gülşah Büyük
Date : 24.10.2020
"""
p , t = map(int , input().split())
case = 0
for i in range(p):
    test = True
    for j in range(t):
        line = input()
        if line[1:].islower() == False:
            test = False
    if test :
        case += 1
print(case)
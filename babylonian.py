"""
Author : Gülşah Büyük
Date : 17.10.2020
"""
n = int((input()))
for i in range(n):
    case =  list(map(str,input().split(",")))
    sexagesimal = 0
    power = len(case)
    for j in range(power):
        if len(case[j])!=0 :
            sexagesimal += int(case[j])*(60**(power-j-1))
    print(sexagesimal)
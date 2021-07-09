"""
Author : Gülşah Büyük
Date : 1.08.2020
"""

decimal = int(input())
for i in range(decimal):
    k,b,n = [int(x) for x in input().split()]
    ssd = 0
    #some squared digits = ssd
    while n>0:
        ssd += (n%b)**2
        n /= b
        n = int(n)
    print(f"{k} {ssd}")
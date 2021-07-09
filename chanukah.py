"""
Author : Gülşah Büyük
Date : 13.10.2020
"""
for i in range(int(input())):
    n,m =[int(x) for x in input().split()]
    candle = int(m*(m+1)/2 + m)
    print(n,candle)



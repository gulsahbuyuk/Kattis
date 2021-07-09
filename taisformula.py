"""
Author : Gülşah Büyük
Date : 25.10.2020
"""
number = int(input())
area = 0.0
sample = 0.0
time = 0.0
for i in range (number) :
    ti,vi = map(float,input().split())
    if i != 0 :
        area = area+float((((sample+vi)/float(2))*(ti-time))/1000)

    sample = vi
    time = ti
print(area)
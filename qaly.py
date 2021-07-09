"""
Author : Gülşah Büyük
Date : 30.07.2020
"""
number = int(input())

qaly = 0. #its float number
qaly=round(qaly,4)
for i in range(number):
    q = [float(y) for y in input().split()]
    qaly += q[0]*q[1]

print(qaly)

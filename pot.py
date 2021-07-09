"""
Author : Gülşah Büyük
Date : 29.07.2020
"""
number = int(input())

sumofpow = 0
for i in range(number):
    num = input()
    sumofpow += int(num[:-1])**int(num[-1])

print(sumofpow)
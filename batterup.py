"""
Author : Gülşah Büyük
Date : 30.07.2020
"""
division = int(input())
number = input().split()

total = 0.

for i in number:
    if int(i)==-1:
        division -= 1
    else:
        total += int(i)
percentage = total/division
print(percentage)
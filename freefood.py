"""
Author : Gülşah Büyük
Date : 16.10.2020
"""

eventNo = int(input())
eventDays = set()
for i in range(eventNo):
    a,b =[int(x)for x in input().split()]
    for i in range (a,b+1):
        eventDays.add(i)
print(len(eventDays))







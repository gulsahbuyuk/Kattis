"""
Author : Gülşah Büyük
Date : 14.10.2020
"""
number = int(input())
listnames = []
temp = []
for i in range(number):
    name = input()
    listnames.append(name)
    temp.append(name)

temp.sort()
if temp[::-1] == listnames:
    print("DECREASING")
elif temp == listnames:
    print("INCREASING")
else:
    print("NEITHER")
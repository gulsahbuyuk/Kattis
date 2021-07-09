"""
Author : Gülşah Büyük
Date : 29.07.2020
"""
number = int(input())

for i in range(number):
    num = int(input())
    if num%2==0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
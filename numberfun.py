"""
Author : Gülşah Büyük
Date : 30.07.2020
"""

num = int(input())

for _ in range(num):
    a,b,c = [(int(x)) for x in input().split()]

    if a+b==c:
        print("Possible")
    elif a / b == c or b / a == c:
        print("Possible")
    elif a-b==c or b-a==c:
        print("Possible")
    elif a*b==c:
        print("Possible")

    else:
        print("Impossible")
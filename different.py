"""
Author : Gülşah Büyük
Date : 15.10.2020
"""

try :
    while True :
        a, b = [int(x) for x in input().split()]
        print(abs(a - b))

except EOFError:
    pass

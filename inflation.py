"""
Author : Gülşah Büyük
Date : 6.08.2020
"""

def inflation(lis):
    m = 1
    for i, x in enumerate(lis):
        if i + 1 < x:
            return -1
        else:
            m = min(m, x / (i+1))
    return m


n = int(input())
i = inflation(sorted(map(int, input().split())))
if i < 0:
    print('impossible')
else:
    print('%.6f' % i) #0dan sonra kaç decimal olacağını belirtmek için formatlı yazım şekli
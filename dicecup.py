"""
Author : Gülşah Büyük
Date : 3.07.2020
"""
from collections import Counter

a,b = [int(x) for x in input().split()]

n = [x for x in range (1,a+1)]
m = [x for x in range (1,b+1)]

c=[]
for i in n :
    for j in m :
        c.append(i+j)

c=Counter(c)

for i in c.most_common():
    if i[1]==c.most_common(1)[0][1]: ## ardaya bu satırdan sonrasını sor!!
        print(i[0])
    else:
        break



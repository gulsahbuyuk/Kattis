"""
Author : Gülşah Büyük
Date : 24.10.2020
"""

x=[int(x) for x in  input().split()]
y=[int(x) for x in input().split()]
minval = min(x[i]/y[i]for i in range(3))
for i in range(3):
    print('{0:.4f}'.format(x[i]-y[i]*minval) )



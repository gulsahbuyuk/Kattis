"""
Author : Gülşah Büyük
Date : 4.08.2020
"""

a,b,c =[int(x) for x in input().split()]

if a+b==c :
    print(f"{a}+{b}={c}")
elif b+c==a :
    print(f"{a}={b}+{c}")
elif a*b==c :
    print(f"{a}*{b}={c}")
elif b*c==a :
    print(f"{a}={b}*{c}")
elif a-b==c :
    print(f"{a}-{b}={c}")
elif a/b==c:
    print(f"{a}/{b}={c}")
elif  b/c==a :
    print(f"{a}={b}/{c}")
elif b-c==a:
    print(f"{a}={b}-{c}")





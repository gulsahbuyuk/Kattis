"""
Author : Gülşah Büyük
Date : 5.09.2020
"""

from itertools import combinations #sayılara ikili kombinasyonlar olarak bak
from collections import  Counter
import sys


def main():
    n,t= [int(x) for x in input().split()]

    s=input()

    if t==1 :
        s= sorted([int(x) for x in s.split()])
        iS= 0
        iB = n-1
        small =s[iS]
        big = s[iB]
        while iS !=iB :
            if small +big > 7777 :
                iB -=1
                big= s[iB]
            elif small+big < 7777 :
                iS += 1
                small =s[iS]
            else :
                print("Yes")
                sys.exit()

        print("No")

    elif t==2 :
        s = Counter(s.split())
        if s.most_common(1)[0][1] > 1 :
            print("Contains duplicate")
        else:
            print("Unique")

    elif t==3 :
        s = Counter(s.split())
        if s.most_common(1)[0][1] > n/2 :
            print(s.most_common(1)[0][0])
        else :
            print("-1")

    elif t==4 :
        s= sorted([int(x) for x in s.split()])
        if n%2 != 0 :
            print(s[n//2])
        else :
            print("{} {}".format(s[n//2-1],s[n//2]))
    else:
        s = sorted([int(x) for x in s.split() if len(x)==3])
        print(" ".join([str(x) for x in s]))



if __name__ == '__main__':
    main()
















"""
Author : Gülşah Büyük
Date : 16.07.2020
"""

from collections import Counter


def primeFac(n):
    i = 2
    factors = []
    while i ** 2 <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)

    if n > 1:
        factors.append(n)

    return Counter(factors)


while True:
    try:
        fact, div = [int(x) for x in input().split()]
        if div == 0:
            print(f"{div} does not divide {fact}!")
            continue
        elif div == 1:
            print(f"{div} divides {fact}!")
            continue
        isTrue = False

        primes = primeFac(div)

        for i in primes.most_common():
            counter= 0

            for q in range(i[0],fact+1):
                while q%i[0]==0 :
                    counter+=1
                    q/=i[0]
                if counter>=i[1]:
                    break
            if counter<i[1]:
                print(f"{div} does not divide {fact}!")
                isTrue = True
                break
        if not isTrue :
            print(f"{div} divides {fact}!")

    except EOFError :
        break





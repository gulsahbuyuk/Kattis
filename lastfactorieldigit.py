"""
Author : Gülşah Büyük
Date : 24.08.2020
"""
nums = int(input())


for i in range(nums):
    factoriel = int(input())
    ans = 1

    for x in range(1, factoriel+1):
        x = str(x)
        ans *= int(x[-1])

    ans = str(ans)
    print(ans[-1])
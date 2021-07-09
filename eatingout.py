"""
Author : Gülşah Büyük
Date : 25.10.2020
"""
def main():

    n = [int(x) for x in input().split()]

    if 2*n[0]>=sum(n[1:]):
        print("possible")
    else:
        print("impossible")


main()
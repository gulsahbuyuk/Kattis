"""
Author : Gülşah Büyük
Date : 17.10.2020
"""
while True :
    try :
        size = int(input())
        if size==1 :
            print(1)
        else :
            print(2*(size-1))
    except EOFError:
        break



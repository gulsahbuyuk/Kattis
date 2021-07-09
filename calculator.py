"""
Author : Gülşah Büyük
Date : 17.10.2020
"""
while True :
    try:
        print("{:.2f}".format(eval(input())))
    except EOFError :
        break

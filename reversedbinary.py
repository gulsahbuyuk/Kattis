"""
Author : Gülşah Büyük
Date : 30.07.2020
"""

number = int(input())
number = bin(number)[:1:-1] #convert binary number
number = int(number,base=2) #converts binary back to a "base=2" number / back to normal form
print(number)
"""
Author : Gülşah Büyük
Date : 12.07.2021
"""
word = input()
unique = set(word)

if len(word)== len(unique):
    print("1")
else:
    print("0")
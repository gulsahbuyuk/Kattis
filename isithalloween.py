"""
Author : Gülşah Büyük
Date : 1.08.2020
"""

month , day = input().split()

if (month == "OCT" and day == "31") or (month == "DEC" and day == "25"):
    print("yup")
else:
    print("nope")
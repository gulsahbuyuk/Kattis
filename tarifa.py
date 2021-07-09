"""
Author : Gülşah Büyük
Date : 3.07.2020
"""

megabyte =int(input())
months =int(input())

ans=0
while months>0 :
    use = int(input())
    ans+= megabyte - use
    months -= 1

print(ans+megabyte)
"""
Author : Gülşah Büyük
Date : 14.10.2020
"""
name = input()
out = ""
for i in range(1,len(name)+1):
    letter = name[i-1]
    if (len(out)>0):
        if (letter != out[len(out)-1]):
            out+= letter
    else:
        out += letter
print(out)
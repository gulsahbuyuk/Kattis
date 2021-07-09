"""
Author : Gülşah Büyük
Date : 7.08.2020
"""
quadkey = input()
x = 0
y = 0 #for starting point
lvl = len(quadkey)
for i in range(lvl):
    s= int(quadkey[lvl - i -1]) #it writes the quadkey in opposite way like if quadkey=130 s=[0,3,1]
    if s ==0 :
        pass
    elif s == 1:
        x += int(2**i) #this is the formula
    elif s==2 :
        y += int(2**i)
    elif s==3 :
        x += int(2**i)
        y+= int(2**i)


print(lvl,x,y)
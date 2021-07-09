"""
Author : Gülşah Büyük
Date : 29.07.2020
"""
text = input().split(" ")
duplicate = False
for i in range(len(text)):
    y = text[i]
    for x in range(len(text)):
        if i == x:
            pass
        else:
            if y == text[x] and not duplicate:
                print("no")
                duplicate = True
                break

if not duplicate:
    print("yes")
##duplicate koyma nedeni içinde olup olmadığını döndürürken süreli bastırmayı engelleyip gerekeen yerde basılmasını sağlamak.
## split string olduğu için "" ile ayrıldı
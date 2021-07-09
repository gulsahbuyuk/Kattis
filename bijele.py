"""
Author : Gülşah Büyük
Date : 14.10.2020
"""

pieces = input().split()
need =(1,1,2,2,2,8)
king = 1-int(pieces[0])
queen = 1-int(pieces[1])
rooks = 2-int(pieces[2])
bishops = 2-int(pieces[3])
knight = 2-int(pieces[4])
pawns = 8-int(pieces[5])
print(king,queen,rooks,bishops,knight,pawns)


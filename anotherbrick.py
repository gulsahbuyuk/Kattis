"""
Author : Gülşah Büyük
Date : 16.10.2020
"""
def main ():
    heightWall,widthWall,noBrick = [int(x) for x in input().split()]
    data = list(map(int,input().split()))

    hight ,length = 0,0
    hls = False
    for i in data :
        length += i
        if length == widthWall :
            length = 0
            hight += 1
            if hight == heightWall :
                hls = True
                break
        if length > widthWall :
            break
    print("YES" if hls else "NO")

main()
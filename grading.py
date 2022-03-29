a,b,c,d,e = [int(x) for x in input().split()]
score = int(input())


if score >= a:
    print("A")
elif (score >= b) and (score < a):
    print("B")
elif (score >= c) and (score < b):
    print("C")
elif (score >= d) and (score < c):
    print("D")
elif (score >= e) and (score < d):
    print("E")
else :
    print("F")




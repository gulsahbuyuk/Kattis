n, x, y = [int(x) for x in input().split()]
# print(x)
for i in range(n):
    a = int(input())
    p = (a/x)*y
    print(int(p))
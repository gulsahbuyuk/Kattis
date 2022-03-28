gunnar = [int(x) for x in input().split()]
emma = [int(x) for x in input().split()]

g = 0
e = 0
for i in gunnar:
    g += i

for j in emma :
    e += j

if e > g :
    print("Emma")
elif e == g :
    print("Tie")
else :
    print("Gunnar")

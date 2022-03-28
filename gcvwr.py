g, t, n = [int(x) for x in input().split()]
weights = [int(x) for x in input().split()]

sum = 0
for i in weights :
    sum += i

w = (g-t)*0.9
ans = w-sum
print(int(ans))


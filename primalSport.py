x = int(input())
lp = [0 for x in range(x+1)]
for i in range(2, x+1):
    if(lp[i]==0):
        for j in range(i*2, x+1, i):
            lp[j] = i
    lp[i] = i - lp[i] + 1
p = x
for i in range(lp[x], x+1):
    p = min(p, lp[i])
print(p)

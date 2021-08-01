n, m = map(int, input().split())
li = list(map(int, input().split()))
res = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if li[i] + li[j] + li[k] > m:
                continue
            else:
                res = max(res, li[i] + li[j] + li[k])
    
print(res)
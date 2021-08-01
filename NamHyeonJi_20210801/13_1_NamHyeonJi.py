n, k = map(int, input().split())
li = []
cnt = 0
for i in range(n):
    li.append(int(input()))
for i in range(n-1, -1, -1):
    if k == 0:
        break
    if li[i] > k:
        continue
    cnt += k // li[i]
    k %= li[i]
print(cnt)
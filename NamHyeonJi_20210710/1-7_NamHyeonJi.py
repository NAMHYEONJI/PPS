#n개 창문, m층 
#그냥 풀었다

m, n = map(int, input().split())
win = [input() for _ in range(5*m+1)]
li = [0]*5

cnt = 0
for i in range(1, 5*n+1, 5):
    for j in range(1, 5*m+1):
        if win[j][i] =='*':
            cnt += 1
        if j % 5 == 0:
            li[cnt] += 1
            cnt = 0

for i in li:
    print(i, end=' ')
            
n, k = map(int, input().split())

li = [i for i in range(n)]
cnt = 1
length = len(li)
i = 0
res = []
print("<", end='')
while True :
    if length == 1:
        break
    if cnt % k == 0:
        print(li[i]+1, end=', ')
        li.remove(li[i])
    else:
        i+=1
    cnt+=1
    length = len(li)
    if length == i:
        i = 0
print(li[0]+1, end='')
print(">")
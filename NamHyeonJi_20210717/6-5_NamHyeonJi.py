n = int(input())
li = list(map(int, input().split()))

li = list(set(li))
li.sort()
for i in range(len(li)):
    print(li[i], end=' ')
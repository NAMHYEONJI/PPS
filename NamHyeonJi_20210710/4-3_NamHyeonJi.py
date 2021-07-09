#뭔가 더 간단하게 풀 수 있을 것 같은데,,,
li = []
cnt = 0
for i in range(10):
    n = int(input())
    re = n%42
    if i == 0:
        cnt+=1
        li.append(re)
    check = 0
    for j in range(len(li)):
        if li[j] == re:
            check = 1
    if check == 0 :
        cnt+=1
        li.append(re)

print(cnt)


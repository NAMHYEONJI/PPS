def cal(n, k):
    li = [0] * k
    res = 0
    for i in range(n):
        for j in range(k):
            if i == 0:
                li[j] = j+1
            else:
                if j == 0:
                    li[j] = 1
                else:
                    li[j] = li[j-1] +li[j]
    for i in range(k):
        res += li[i]

    return res

t = int(input())

for i in range(t):
    n= int(input())
    k= int(input())
    print(cal(n, k))

#코드가 너무 지저분하다
n = int(input())

def aver_cal(x):
    sum = 0
    for i in range(1, x[0]+1):
        sum += x[i]
    aver = sum / x[0]
    cnt = 0
    for i in range(1, x[0]+1):
        if aver < x[i]:
            cnt += 1
    return cnt/x[0] * 100


for i in range(n):
    inp = list(map(int,input().split()))
    print("{:.3f}%".format(aver_cal(inp)))
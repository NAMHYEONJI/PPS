#괜찮았다
n = int(input())
def mars_cal(x):
    for i in range(len(x)):
        if i == 0:
            res = float(x[i])
        elif x[i] == '@':
            res=res*3
        elif x[i] == '%':
            res=res+5
        elif x[i] == '#':
            res=res-7
    return res
    
for i in range(n):
    exp = list(map(str, input().split()))
    print('{:.2f}'.format(mars_cal(exp)))
    
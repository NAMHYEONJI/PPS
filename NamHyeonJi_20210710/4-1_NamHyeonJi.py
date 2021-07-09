#괜찮았다
def sum(x):
    s = 0
    for i in range(4):
        s+= x[i]
    return s
max = 0
idx = 0
for i in range(5):
    score = list(map(int, input().split()))
    s = sum(score)
    if s > max :
        max = s
        idx = i

print(idx+1, max)

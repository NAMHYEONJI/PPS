n = int(input())

def score_cal(x):
    score = 0
    before = 0
    for i in x:
        if i == 'O':
            if before != -1:
                before += 1
                score += before
            else:
                before = 1
                score += before
        else:
            before = -1
    return score
sc =input()


for i in range(n-1):
    print(score_cal(sc))
    sc = input()
print(score_cal(sc))    

def solution(start, end):
    if start > end:
        return

    division = end+1

    for i in range(start+1, end+1):
        if res[start] < res[i]:
            division = i
            break
    #print(division)

    solution(start+1, division-1)
    solution(division, end)
    print(res[start])


import sys
sys.setrecursionlimit(10 ** 9)

res = []
cnt = 0

while cnt <= 10000:
    try:
        num = int(input())
    except:
        break
    res.append(num)
    cnt+=1

solution(0, len(res)-1)

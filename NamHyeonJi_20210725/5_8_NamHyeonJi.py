def divisor(n):
    cnt = 0
    for i in range(1, n+1):
        if n%i == 0:
            cnt += 1
    return cnt

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        div_cnt = divisor(i)
        if div_cnt%2 == 0:
            answer+=i
        else:
            answer-=i

    return answer

print(solution(13,17))
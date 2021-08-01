def solution(x):
    s = str(x)
    sum = 0
    for i in s:
        sum+=int(i)
    if x % sum == 0:
        return True
    else:
        return False

print(solution(11))
def is_decimal(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    else:
        return True

def solution(nums):
    answer = 0
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                if is_decimal(nums[i]+nums[j]+nums[k]):
                    answer += 1

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    
    return answer
# nums=[1,2,7,6,4]
# print(solution(nums))



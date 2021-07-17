def solution(cookie):
    max_sum = 0

    for i in range(len(cookie) - 1):
        left, left_i = cookie[i], i
        right, right_i = cookie[i + 1], i + 1

        while True:
            if left == right:
                max_sum = max(max_sum, left)
            if left <= right and left_i > 0:
                left_i -= 1
                left += cookie[left_i]
            elif right <= left and right_i < len(cookie) - 1:
                right_i += 1
                right += cookie[right_i]
            else:
                break

    return max_sum

cookie = [1,1,2,3]
print(solution(cookie))


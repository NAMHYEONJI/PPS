def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    nums.sort()
    cnt = 0
    max_cnt = 0
    max_val = 0
    for i in range(len(nums)):
        if i == 0:
            cnt = 1
        else:
            if nums[i] == nums[i-1]:
                cnt += 1
            else:
                cnt = 1
        # print(cnt, nums[i])
        if max_cnt < cnt:
            max_cnt = cnt
            max_val = nums[i]
    return max_val
nums = [2,2,1,1,1,2,2]
print(majorityElement(nums))
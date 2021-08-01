def maxSubArray(nums):
    cur = maxs = nums[0]
    for i in nums[1:]:    
        cur = max(i, cur+i)
        maxs = max(maxs, cur)
    
    return maxs
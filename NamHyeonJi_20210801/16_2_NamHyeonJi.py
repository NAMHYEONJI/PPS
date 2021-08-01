def findDisappearedNumbers(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    li = list(range(1,len(nums)+1))
    
    res = []
    for i in nums:
        li[i - 1] = 0
    for i in li:
        if i != 0:
            res.append(i)
    return res


nums = [4,3,2,7,8,2,3,1]
print(findDisappearedNumbers(nums))
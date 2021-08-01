def sortArrayByParityII(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    even = []
    odd = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            even.append(nums[i])
        else:
            odd.append(nums[i])
    res = []
    for i in range(int(len(nums)/2)):
        res.append(even[i])
        res.append(odd[i])
    return res

nums = [4,2,5,7]
print(sortArrayByParityII(nums))
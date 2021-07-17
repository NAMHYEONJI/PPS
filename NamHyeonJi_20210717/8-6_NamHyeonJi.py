def searchInsert(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums)
        while start < end:
                mid = ((end-start)//2) +start
                if target == nums[mid]:
                        return mid
                elif target > nums[mid]:
                        start = mid+1
                elif target < nums[mid]:
                        end = mid
        
        return start
        
nums = [1,3,5,6]
target = 7
print(searchInsert(nums, target))
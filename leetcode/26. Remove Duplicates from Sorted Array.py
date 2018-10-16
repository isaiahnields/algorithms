class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        i = 0
        j = 1
        
        if not nums:
            return 0
        
        while j < len(nums):
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
            if j < len(nums):
                i += 1
                nums[i] = nums[j]
                
        return i + 1

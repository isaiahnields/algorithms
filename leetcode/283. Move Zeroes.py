class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        j = -1
        for i, v in enumerate(nums):
            if v != 0:
                j += 1
                nums[j], nums[i] = nums[i], nums[j]

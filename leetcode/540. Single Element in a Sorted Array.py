class Solution:
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while r > l:
            c = (r + l) // 2
            if nums[c] == nums[c ^ 1]: l = c + 1
            else: r = c
        return nums[r]

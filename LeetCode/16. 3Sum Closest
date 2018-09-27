class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest = float('inf')
        for i in range(1, len(nums) - 1):
            l, r = 0, len(nums) - 1
            while l < i < r:
                summ = nums[l] + nums[i] + nums[r]
                if abs(summ - target) < abs(closest - target):
                    closest = summ
                if summ > target:
                    r -= 1
                elif summ < target:
                    l += 1
                else:
                    return summ
        return closest

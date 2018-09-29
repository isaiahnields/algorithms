class Solution:
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        return list(map(self.helper, [i for i in range(num + 1)]))
        
    def helper(self, num):
        count = 0
        while num:
            count += num & 1
            num = num >> 1
        return count

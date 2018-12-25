class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        seen = set()
        for i in A:
            if i in seen:
                return i
            seen.add(i)

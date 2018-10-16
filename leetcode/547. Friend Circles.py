class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        count = 0
        for r in range(len(M)):
            if self.helper(M, r):
                count += 1
        
        return count
    
    
    def helper(self, M, r):
        connected = set()
        for c in range(len(M)):
            if M[r][c] == 1:
                M[r][c] = 0
                connected.add(c)
                connected |= self.helper(M, c)
    
        return connected

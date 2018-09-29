class Solution:
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        
        M, N = len(matrix), len(matrix[0])
        maxx = 0
        mem = dict()
        for r in range(M):
            for c in range(N): 
                maxx = max(self.helper(matrix, r, c, M, N, mem), maxx)
                
        return maxx
    
    def helper(self, matrix, r, c, M, N, mem):
        maxx = 1
        
        if (r, c) in mem:
            return mem[(r, c)]
        
        if r + 1 < M and matrix[r + 1][c] > matrix[r][c]:
            maxx = max(maxx, self.helper(matrix, r + 1, c, M, N, mem) + 1)
            
        if r - 1 >= 0 and matrix[r - 1][c] > matrix[r][c]:
            maxx = max(maxx, self.helper(matrix, r - 1, c, M, N, mem) + 1)
            
        if c + 1 < N and matrix[r][c + 1] > matrix[r][c]:
            maxx = max(maxx, self.helper(matrix, r, c + 1, M, N, mem) + 1)
            
        if c - 1 >= 0 and matrix[r][c - 1] > matrix[r][c]:
            maxx = max(maxx, self.helper(matrix, r, c - 1, M, N, mem) + 1)
            
        mem[(r, c)] = maxx
        
        return maxx

class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        M, N, maxx = len(grid), len(grid[0]), 0
        for r in range(M):
            for c in range(N):
                maxx = max(self.helper(grid, r, c, M, N), maxx)
        return maxx
    
    def helper(self, grid, r, c, M, N):
        if not 0 <= r < M or not 0 <= c < N or grid[r][c] != 1:
            return 0
        grid[r][c] = -1
        summ = self.getPerimeter(grid, r, c, M, N)
        for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            summ += self.helper(grid, r + i, c + j, M, N)
        return summ
    
    def getPerimeter(self, grid, r, c, M, N):
        summ = 0
        for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            if (not 0 <= r + i < M or not 0 <= c + j < N) or grid[r + i][c + j] == 0:
                summ += 1
        return summ

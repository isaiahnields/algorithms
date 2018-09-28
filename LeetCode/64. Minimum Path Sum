class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        return self.helper(grid, 0, 0, dict())
    
    
    def helper(self, grid, r, c, mem):
        if r == len(grid) - 1 and c == len(grid[0]) - 1:
            return grid[r][c]
        if (r, c) in mem:
            return mem[(r, c)]
        if not 0 <= r < len(grid) or not 0 <= c < len(grid[0]):
            return float('inf')
        mem[(r, c)] = min(self.helper(grid, r + 1, c, mem) + grid[r][c], self.helper(grid, r, c + 1, mem) + grid[r][c])
        return mem[(r, c)]

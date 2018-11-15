class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.M, self.N, self.board = len(board), len(board[0]) if len(board) else 0, board
        for m in range(self.M):
            for n in range(self.N):
                if self.dfs(m, n, word, 0, set()):
                    return True
        return False
    
    def dfs(self, m, n, word, idx, visited):
        if len(word) == idx: return True
        if not 0 <= m < self.M or not 0 <= n < self.N or (m, n) in visited or self.board[m][n] != word[idx]: return False
        
        visited.add((m, n))
        
        res = any(self.dfs(m + i, n + j, word, idx + 1, visited) for i, j in [(0, 1), (1, 0), (0, -1), (-1, 0)])
        
        visited.remove((m, n))
        
        return res

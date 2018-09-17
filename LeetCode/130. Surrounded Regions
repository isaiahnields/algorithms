class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m, n = len(board), len(board[0])
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O' and self.enclosed(board, r, c):
                    self.sink(board, r, c)
                    
        for r in range(m):
            for c in range(n):
                if board[r][c] == 'C':
                    board[r][c] = 'O'
        
                    
    def sink(self, board, r, c):
        m, n = len(board), len(board[0])
        if board[r][c] == 'X':
            return
        
        board[r][c] = 'X'
        
        self.sink(board, r + 1, c)
        self.sink(board, r - 1, c)
        self.sink(board, r, c + 1)
        self.sink(board, r, c - 1)
        
                    

    def enclosed(self, board, r, c):
        m, n = len(board), len(board[0])
        if not 0 <= r < m or not 0 <= c < n:
            return False
        
        if board[r][c] == 'X' or board[r][c] == 'C':
            return True
        
        board[r][c] = 'C'
        
        res = [self.enclosed(board, r + 1, c),
               self.enclosed(board, r - 1, c),
               self.enclosed(board, r, c + 1),
               self.enclosed(board, r, c - 1)]
        
        return all(res)

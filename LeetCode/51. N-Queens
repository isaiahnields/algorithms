class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = Board(n)
        res = []
        self.helper(board, 0, res)
        return res
    
    def helper(self, board, row, res):
        if row < board.size:
            for c in range(board.size):
                if board.add(Queen(row, c)):
                    self.helper(board, row + 1, res)
                    board.remove(Queen(row, c))
        else:
            res.append(board.get_board())

class Queen:
    
    def __init__(self, row, column):
        self.row = row
        self.column = column
        
    def __eq__(self, queen):
        if self.row == queen.row and self.column == queen.column:
            return True
        else:
            return False
        
    def __hash__(self):
        return hash((self.row, self.column))
        
    def getDiagonalUp(self):
        return self.column + self.row
    
    def getDiagonalDown(self):
        return self.row - self.column
    
    def isAttackable(self, position):
        if position.row == self.row or \
        position.column == self.column or \
        self.getDiagonalDown() == position.getDiagonalDown() or \
        self.getDiagonalUp() == position.getDiagonalUp():
            return True
        return False
        
class Board:
    
    def __init__(self, n):
        self.queens = set()
        self.size = n
    
    def get_board(self):
        board = []
        for r in range(self.size):
            row = ''
            for c in range(self.size):
                if Queen(r, c) in self.queens: row += 'Q'
                else: row += '.'
            board.append(row)
        return board
        
    def add(self, piece):
        for queen in self.queens:
            if queen.isAttackable(piece): return False
        self.queens.add(piece)
        return True
    
    def remove(self, piece):
        self.queens.remove(piece)

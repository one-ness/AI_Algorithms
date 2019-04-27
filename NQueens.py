def NQueens(n):
    output = []
    def dfs(row, queens, diags):
        if row == n:
            output.append(['.'*x + 'Q' + '.'*(n-x-1) for x in queens])
            return
        for col in range(n):
            if not any([row+col in diags, row-col-n-1 in diags, col in queens]):
                dfs(row + 1, queens + [col], diags | {row+col, row-col-n-1})
    dfs(0, [], set())
    return output

def solveNQueens(n):
    output = []
    board = QueenBoard(n)
    def dfs(row):
        if row == n:
            output.append(board.print())
            return
        for col in range(n):
            if board.validMove(row, col):
                board.add(row, col)
                dfs(row + 1)
                board.remove(row, col)
    dfs(0)
    return output

class QueenBoard:
    def __init__(self, n):
        self.queen_board = []
        self.cols = set()
        self.r_diagonal = set()
        self.l_diagonal = set()
        self.n = n
    def add(self, row, col):
        self.queen_board.append(col)
        self.cols.add(col)
        self.r_diagonal.add(row + col)
        self.l_diagonal.add(row - col)
    def remove(self, row, col):
        self.cols.remove(col)
        self.r_diagonal.remove(row + col)
        self.l_diagonal.remove(row - col)
        self.queen_board.pop()
    def validMove(self, row, col):
        return col not in self.cols and \
                row + col not in self.r_diagonal and \
                row - col not in self.l_diagonal
    def print(self):
        return ['-'*x + 'Q' + '-'*(self.n-x-1) for x in self.queen_board]

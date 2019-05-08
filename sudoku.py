def solveSudoku(n, board):
    output = []
    def constructBoard(n, board):
        s = Sudoku(board, n)
        for i in range(n):
            for j in range(n):
                if board[i][j] != 0:
                    if i in s.rows:
                        s.rows[i].add(board[i][j])
                    else:
                        s.rows[i] = {board[i][j]}
                    if j in s.cols:
                        s.cols[j].add(board[i][j])
                    else:
                        s.cols[j] = {board[i][j]}
                    square = int(i / 3) * 3 + int(j / 3)
                    if square in s.squares:
                        s.squares[square].add(board[i][j])
                    else:
                        s.squares[square] = {board[i][j]}
        return s
    sudoku = constructBoard(n, board)

    def solve(sudoku):
        row, col = openSquare(sudoku.sudoku_board, n)
        if row == -1:
            return True
        for num in range(1, n + 1):
            if sudoku.validMove(num, row, col):
                sudoku.add(num, row, col)
                if(solve(sudoku)):
                    return True
                sudoku.remove(num, row, col)
        return False
    if(solve(sudoku)):
        for i in range(n):
            if i % 3 == 0:
                for k in range(n + 3):
                    print('_', end='')
                print()
            for j in range(n):
                if j % 3 == 0:
                    print('|',end='')
                print(sudoku.sudoku_board[i][j], end='')
            print('|')
        for k in range(n + 3):
            print('_', end='')
        print()
    else:
        print("Fail")

def openSquare(board, n):
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                return i, j
    return -1, -1

class Sudoku:
    def __init__(self, board, n):
        self.sudoku_board = board
        self.cols = dict()
        self.rows = dict()
        self.squares = dict()
        self.n = n
    def add(self, num, row, col):
        self.cols[col].add(num)
        self.rows[row].add(num)
        self.squares[int(row/3) * 3 + int(col / 3)].add(num)
        self.sudoku_board[row][col] = num
    def remove(self, num, row, col):
        self.cols[col].remove(num)
        self.rows[row].remove(num)
        self.squares[int(row/3) * 3 + int(col / 3)].remove(num)
        self.sudoku_board[row][col] = 0
    def validMove(self, num, row, col):
        return num not in self.cols[col] and \
                num not in self.rows[row] and \
                num not in self.squares[int(row / 3) * 3 + int(col / 3)]

def main():
    rows = dict()
    board = []
    board.append([3,0,6,5,0,8,4,0,0])
    board.append([5,2,0,0,0,0,0,0,0])
    board.append([0,8,7,0,0,0,0,3,1])
    board.append([0,0,3,0,1,0,0,8,0])
    board.append([9,0,0,8,6,3,0,0,5])
    board.append([0,5,0,0,9,0,6,0,0])
    board.append([1,3,0,0,0,0,2,5,0])
    board.append([0,0,0,0,0,0,0,7,4])
    board.append([0,0,5,2,0,6,3,0,0])

    solveSudoku(9, board)
    
if __name__ == '__main__':
    main()

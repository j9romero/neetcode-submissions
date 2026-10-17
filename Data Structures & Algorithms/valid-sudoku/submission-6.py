class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)

        for r in range(9): #need to know the row number
            for c in range(9): #need to know the col number
                if board[r][c] == ".":
                    continue
                if board[r][c] in row[r]:
                    return False
                if board[r][c] in col[c]:
                    return False
                if board[r][c] in square[(r//3, c//3)]:
                    return False
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                square[(r//3,c//3)].add(board[r][c])
        return True


















       


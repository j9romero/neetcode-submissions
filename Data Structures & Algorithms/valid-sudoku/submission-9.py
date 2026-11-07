class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                if val in row[r]:
                    return False
                if val in col[c]:
                    return False
                if val in squares[(r//3, c//3)]:
                    return False
                row[r].add(val)
                col[c].add(val)
                squares[(r//3, c//3)].add(val)
        return True
        
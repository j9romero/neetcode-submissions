class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = -1

        for i, rows in enumerate(matrix):
            n = len(rows)-1
            if rows[0] <= target <= rows[n]:
                row = i
                break
        
        if row == -1:
            return False

        start= 0
        end = len(matrix[row])-1
        while start <= end:
            mid = (start+end)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                end = mid - 1
            elif matrix[row][mid] < target:
                start = mid+1
        return False
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = -1

        for rows in range(len(matrix)):
            if matrix[rows][0] <= target <= matrix[rows][-1]:
                row = rows
        if row == -1:
            return False 
        
        start = 0
        end = len(matrix[row])-1
        while start <= end:
            mid = (start+end) // 2
            if target == matrix[row][mid]:
                return True
            elif target < matrix[row][mid]:
                end = mid -1
            else:
                start = mid + 1
        return False 

        
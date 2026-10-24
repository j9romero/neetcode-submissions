class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = -1
        for i in range(len(matrix)):
            if matrix[i][0] <= target <= matrix[i][-1]:
                row = i
                break
        if row == -1:
            return False

        start = 0
        end = len(matrix[row]) -1

        while start <= end:
            mid = (start+end)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                start = mid +1
            elif matrix[row][mid] > target:
                end = mid -1
        return False

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left_arr = 0
        right_arr = len(matrix) - 1
        while left_arr <= right_arr:
            middle = (left_arr + right_arr) // 2
            if matrix[middle][0] == target:
                return True
            elif matrix[middle][0] < target:
                left_arr = middle + 1
            else:
                right_arr = middle - 1
        if right_arr < 0:
            return False
        left = 0
        right = len(matrix[right_arr]) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[right_arr][mid] == target:
                return True
            elif matrix[right_arr][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
            
        
            
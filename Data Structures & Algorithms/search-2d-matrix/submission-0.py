class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while (l <= r):
            middle = (l + r) // 2
            if target < matrix[middle][0]:
                r = middle - 1
            elif target > matrix[middle][len(matrix[middle]) - 1]:
                l = middle + 1
            else:
                l, r = 0, len(matrix[middle]) - 1
                while l <= r:
                    if target < matrix[middle][(l + r) // 2]:
                        r = ((l + r) // 2) - 1
                    elif target > matrix[middle][(l + r) // 2]:
                        l = ((l + r) // 2) + 1
                    else:
                        return True
        return False
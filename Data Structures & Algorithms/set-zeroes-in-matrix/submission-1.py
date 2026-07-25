class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        def setZeros(r, c):
            for i in range(ROWS):
                matrix[i][c] = '#' if matrix[i][c] != 0 else matrix[i][c]
            for j in range(COLS):
                matrix[r][j] = '#' if matrix[r][j] != 0 else matrix[r][j]

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    setZeros(r, c)
        
        for r in range(ROWS):
            for c in range(COLS):
                matrix[r][c] = 0 if matrix[r][c] == '#' else matrix[r][c]
        
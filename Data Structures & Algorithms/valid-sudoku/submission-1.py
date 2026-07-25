class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols,  = {}, {}

        for i in range(3):
            for j in range(3):
                square = set()
                for row in range(3 * i, 3 * (i + 1)):
                    for col in range(3 * j, 3 * (j + 1)):
                        x = board[row][col]
                        if x == ".":
                            continue 
                        if row not in rows:
                            rows[row] = []
                        if col not in cols:
                            cols[col] = []
                        if x in rows[row] or x in cols[col] or x in square:
                            return False
                        rows[row].append(x)
                        cols[col].append(x)
                        square.add(x)
        return True
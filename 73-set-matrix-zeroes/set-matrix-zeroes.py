class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        first_row_zero = False
        first_col_zero = False

        # Check if first row contains 0
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True

        # Check if first column contains 0
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True

        # Use first row and first column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Make rows zero
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0

        # Make columns zero
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0

        # Finally handle first row
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0

        # Finally handle first column
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
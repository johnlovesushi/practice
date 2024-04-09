class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n,m = len(matrix),len(matrix[0]) # row, col
        self.res = [[0 for _ in range(m+1)] for _ in range(n+1)]
        temp = 0
        for i in range(n):
            for j in range(m):
                self.res[i+1][j+1] = self.res[i][j+1] + self.res[i+1][j] + matrix[i][j] - self.res[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.res[row2+1][col2+1] - self.res[row2+1][col1] - self.res[row1][col2+1] + self.res[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
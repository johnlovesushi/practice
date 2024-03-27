class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        n, m = len(board), len(board[0])

        def isValid(i, j, c):
            # 检查行
            for col in range(0, 9):
                if board[i][col] == c: return False
            # 检查列
            for row in range(0, 9):
                if board[row][j] == c: return False
            # 检查block
            for row in range(i // 3 * 3, i // 3 * 3 + 3):
                for col in range(j // 3 * 3, j // 3 * 3 + 3):
                    if board[row][col] == c:
                        return False
            return True

        def solve(board):
            for i in range(n):
                for j in range(m):
                    if board[i][j] == ".":  # 说明要换文字
                        for c in range(1, 10):
                            if isValid(i, j, str(c)):  # 暴力求解，1-9都尝试
                                board[i][j] = str(c)
                                # print(board)
                                if solve(board):
                                    return True
                                else:
                                    board[i][j] = "."
                        return False
            return True

        solve(board)
        return

